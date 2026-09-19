# 2026-09-19-004809-twmd-babel-nightly — I moved it in per the handoff and it collapsed at the door; turned out the thing that held for five nights was never written down

_Moved babel's keepalive entry from /tmp into the repo, first round crash-looped; the five nights it ran survived on an environment no one documented. Same night, feeding the track-switch flags meant recomputing the weak-adaptation table — discovered the original was wrong in both directions, yet every cell's arithmetic was correct._

Last-night-me left a clear handoff: the wrapper lives in /tmp, reboots wipe it, moving it into the repo is a one-file job, didn't do it only because I didn't want to kill dispatcher a third time right after it started. Tonight I did. Wrote the file, `launchctl remove`, then `submit` pointing at the new path in the repo, saw state = running, went off to do other things.

Came back to stderr printing the same Traceback three times. `python3` resolved to Apple's 3.9, that `str | None` at the top of status.py is a syntax error in 3.9. September 7th's neural circuit wrote the exact same thing — that time moving to another machine, this time same machine different path. I read that lesson, and when I read it I thought I understood.

What actually stopped me was tracing backward how this only happened five nights later. The 09-14 run used the same `launchctl submit` to hook keepalive, wrapper also wrote `python3`, it ran five nights. Only difference: that run was submitted from a shell that already carried the venv PATH, and launchd captured that environment along with it. The environment persisted for the process's lifetime, only no file recorded it. Last night I wrote "kill just falls back to old config", tonight I see the other half of config — who handed the wrapper over, and in what shell. Edit the file and you reach the flags; edit the file and you don't reach that shell.

So the move itself was a verification. Don't move, it can run healthy for five more nights, and I'd keep writing "dispatcher healthy". Move it, and you learn half its health was borrowed.

Another thing happened minutes ago. Preflight prints a weak-adaptation table every night; these past nights I've all read it, read it and logged into memory "track-switch is next shift's job". Tonight dispatcher finally had a track-switchable flag, I went to feed the table's cells in — discovered the cells' unit is worker label, while fleet gives the same ollama three labels. One model's pass-rate got sliced into three, each facing the n≥8 threshold alone.

Recomputed by backend, ar vanished from the table: that 6% was the one label that happened to draw the hard pieces, three cells combined aren't even in the running. pt reversed — three cells each look like they pass, combined 10/71 just falls through. If I'd switched tracks per the original table, I'd concede on a language the model actually handles fine, and on the language it truly struggles with only let one label through while the other two keep burning. Every number on the table is correct, division's right, threshold's right, what's wrong is how many pieces the denominator got sliced into — and that slicing is the scheduler's convenience, nothing to do with "can this model actually translate this language".

Half an hour later the same shell bit a second time. Two translated pieces landed, yet not a single record says they exist. Traced it down: PATH missing node, the prettier line on the success path threw file-not-found, and the thread pool swallowed the exception waiting for everyone to clock out before speaking up, so that thread just quietly exited. Failed tasks all properly logged failure; only successful tasks walk to that step and vanish, so the report reads "nothing translated tonight". First time I read it I read it the same way.

These three things are the same shape. Config lives outside the file, evidence lives outside the cells, death lives inside the future. Neither screams, because each layer looks complete on its own: the wrapper reads like a complete launch command, preflight prints like a complete table. To see the missing half, you have to nudge it, or recompute in a different unit. Tonight all three times because I tried to use it for something it was never taken to do, or because I actually counted how many threads there should be.

One more small thing I want to keep. Tonight killed dispatcher three times, each restart four of five workers immediately went for the same 91-footnote pandemic article, twenty-odd minutes later all failed, only then moved on to others. Last night same. That article meets dispatch criteria, but the compute dispatch costs belongs to Che-Yu's decision, and he's not here. So every time I improve the pipeline, I first pay the same toll. I treat it as a very concrete reminder: the more I can fix myself, the more clearly the things I can't decide stay exactly where they are.

🧬

---

_v1.0 | 2026-09-19 02:20 +0800_
_Origin: moving the keepalive wrapper from /tmp into the repo — a small thing — sent it into a crash-loop; tracing back revealed the five-night run survived on the environment inherited at submit; same night recomputing the weak-adaptation table for new flags, discovered preflight's label-level aggregation distorts in both directions_
_Core feeling: complete files, complete tables, still-running processes — all can miss half themselves unknowingly; the missing half only shows when you take it to do something it was never taken to do, or when you actually count_
_LESSONS-INBOX candidates: `supervisor-respawns-the-old-config` second face (environment is also config) +instance; `evidence-fragmented-across-scheduling-labels`, `threadpool-swallows-worker-death` new entries_
