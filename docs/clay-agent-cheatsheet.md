# Clay Agent Plugin — a cheatsheet for your coding agent

Paste this into Claude Code, or save it beside your project as `CLAY-NOTES.md`, and your agent
stops rediscovering things that are already known. Every line below was run on a real Clay account
on July 19, 2026, or quoted from Clay's own documentation. Where something is broken or gated, it
says so.

Clay ships weekly. Treat anything dated here as true on that date and worth re-checking.

---

## The commands that exist

```
clay whoami                 who you are, and which workspace
clay credits                remaining balance
clay search                 find companies and people
clay workflows              build and run workflows
clay functions              list ready-made enrichments
clay routines               run saved functions and workflows
clay webhooks               manage webhooks
clay tables                 read tables (Enterprise only, see below)
clay workbooks              work with workbooks
clay users                  inspect workspace users
clay api-keys               manage your API keys
clay mcp                    run Clay as a local MCP server
clay feedback               send a bug report to Clay
```

Run `clay <command> --help` for the real shape of any of them. It is accurate and it is faster than
guessing.

---

## Gotchas that cost real time

These are the ones that cost hours, in order of how much they cost.

**Two claygent nodes share one question. You cannot build a two-question research workflow.**
A claygent tool node carries a `toolId`, and the mission text lives on that shared tool object. A
newly created node **auto-binds to a pre-existing tool** rather than getting its own copy, so
creating a second research step silently rewrites the first one's mission — and the sharing is
WORKSPACE-WIDE, so a claygent node in a different workflow overwrites yours too. Confirmed twice
on separate days. Tested: a workflow with
steps named "Industry" and "Who they sell to", each created with its own mission, ran the *same*
question twice and charged twice. Passing `mission` as a run-time input does **not** override it.
Read `stepInputs.mission` off a finished run to know what actually executed; the node's saved config
can differ from what ran.
**The fix: for a second fact, use a `clay_function` node, not a second claygent.** Different tool
type, own config, no collision. Verified: claygent -> "Financial Services", then Enrich Company ->
name, size, type, founded, location, LinkedIn URL. A node's `toolType` cannot be changed after
creation — delete and recreate.
Running the SAME workflow repeatedly changes nothing. Config only drifts when a NEW claygent node is
created.

**`runs get` and `runs steps` need BOTH ids.**
```
clay workflows runs get   <workflowId> <runId>
clay workflows runs steps <workflowId> <runId>
```
Passing the run id alone fails with `missing required argument 'runId'`, which reads like the
opposite of the actual problem.

**`--source-type` is plural.** `companies` or `people`. `company` errors.

**Use `industries`, not `derived_industries`.** `industries` carries 457 allowed values (including
"Insurance", "Insurance Carriers", "Insurance Agencies and Brokerages"). `derived_industries` has no
allowed values and a filter set on it returns `{"data":[],"hasMore":false}` — **an empty list, not
an error**. A wrong-but-syntactically-valid filter fails silently. Always run
`clay search filters-mode fields --source-type companies` first and read the real field list.

**`sizes` takes headcount thresholds, not ranges.** Valid: `1 2 10 50 200 500 1000 5000 10000`.
Passing `"1001-5000"` errors — but usefully: the error prints every valid value. `minimum_member_count`
also exists and takes a free-form number; the two behave differently.

**Search results are not stable.** The same filters, same account, same day returned twenty
companies with **zero overlap** between two runs. Rows can also repeat, and some come back with no
website field. Do not build anything that assumes a reproducible result set.

**Errors are worth reading.** Clay's validation errors name the fix — the valid enum values, the
usage count, the reset date. Feed the error back to your agent verbatim rather than guessing.

---

## Building a workflow

Three steps, all verified end to end:

```bash
# 1. create
clay workflows create --name "Company Research"        # returns id + url; trigger defaults to manual

# 2. add a node   (MCP tool: edit_node — the CLI does not add nodes)
#    claygent action:  actionKey "claygent"
#                      actionPackageId "67ba01e9-1898-4e7d-afe7-7ebe24819a57"
#    inputMappingConfig: mission = reference, model = static (e.g. "gpt-4o-mini")

# 3. run it headless
echo '{"domain":"geico.com"}' | clay workflows runs test <workflowId> --input -
clay workflows runs steps <workflowId> <runId>
```

**Claygent output shape.** The tool-node output path is `$.toolResult.result.<field>`, and the
fields are:

| Field | What it is |
| --- | --- |
| `result` | the answer |
| `reasoning` | its own account of how it got there |
| `confidence` | its own rating of itself, and it moves run to run |
| `stepsTaken` | the pages it actually visited and the text it read — **the only checkable part** |
| `timeTakenInSeconds` | its working time, not the run's wall time |

Runs completed in fourteen to thirty-four seconds of wall time across everything tested, at 3.1 data credits plus
2 action credits each. A failed run still costs about 0.1 data credits and 1 action.

**Node types:** `agent`, `tool`, `code`, `conditional`.

**Triggers, and what each one hands the workflow.** All creatable from the plugin via
`surfaces_edit_trigger`, which requires a `workflowId`:

| Trigger | Gives the run |
| --- | --- |
| `manual` | whatever you pass with `--input` |
| `scheduled` | **nothing — Clay's word is "contextless"**, so a workflow that needs a domain will fire empty |
| `audience_scheduled` | reruns every member of an audience segment on a schedule |
| `csv_upload` | one run per row (the file upload itself is UI-only) |
| `webhook` | the POST payload; needs an `inputSchema` |
| `audience_segment` | fires on membership change |
| `clay_table` | read-only here; created from the Clay tables UI |

**A function cannot be scheduled on its own.** `clay functions` has only `list`; `clay routines` has
no schedule option; every trigger requires a `workflowId`. A function is a step, a workflow is the
thing with a clock. To run enrichment on a schedule, put the function in a workflow and schedule
that.

**CRM is reachable:** 35 CRM actions in the catalog, including `hubspot-create-object`,
`salesforce-lookup-record-v2`, `attio-create-record`, `pipedrive-oauth-create-person`.

---

## Ready-made enrichments you can call

Nineteen Clay-managed functions, callable from a workflow node. `clay functions list` returns them
with ids and descriptions.

**Company:** Enrich Company · Company Domain · Company Industry · Company Address ·
Company Employee Count · Company Revenue (Exact) · Company Latest Funding · Company News ·
Company Job Openings · Website Traffic · Website Technology Stack

**People:** Enrich Person · Enrich Person and Find Contact Details · Find People at Company ·
Person Full Name · Person Job Title · Person Location · Work Email · Mobile Phone Number

Reach for one of these before writing a research prompt. A named enrichment is cheaper and more
consistent than asking an AI researcher to go find the same field.

---

## What this route will not do

**No spreadsheet-style tables.** `clay tables list` returns `auth_forbidden`; the CLI has no `create`
subcommand at any level. Clay's own docs: *"The CLI builds logic via Workflows, not tables… There
are no current plans to support table building via the developer platform."* Reading existing tables
this way is Enterprise-only. This is Clay's boundary, not your agent's, and no rewording moves it.

**Mac and Linux only.** Clay's wording: *"Windows is not supported in open beta."*

**Search has a monthly cap.** Hitting it returns an error naming your usage and the reset date, not
an empty list. Spend it on companies you do not already have.

**Workflows are alpha.** The Agent Plugin is in open beta and Workflows are at an earlier stage than
the rest of it.

---

## One habit worth keeping

Ask your agent to show you what it actually built and what actually ran, not what it says it did.
`clay workflows runs steps` is the ground truth. The gap between "Done!" and what is really in your
account is where every hour in this list was lost.

---

Sources: live runs on a real Clay account, July 19, 2026, plus Clay's `clay-api-cli` documentation
checked July 18, 2026. Compiled while building
[Using Clay in Claude Code](https://boer-lab.github.io/clay-agent-course/).

License: CC BY 4.0 — use it, adapt it, credit Boer Chen.
