# Foundation workflow — ChatGPT-operated, auditable

## Entry -> exit

| Step | Trigger / input | Lead role | Artefakt | Exit gate |
|---|---|---|---|---|
| 0 Baseline | mavjud design evidence | Critical Reviewer | baseline audit | Dalil yoki `UNSCORED` sababi |
| 1 Brief | product goal, constraints | UX Researcher | design brief | User/task/success metric aniq |
| 2 Research | brief + source URLs | UX Researcher | reference cards | URL, observation, caution |
| 3 Concepts | approved brief + references | Creative Director | 2 distinct directions | Difference/tradeoff recorded |
| 4 Architecture | selected direction | Design Architect | tokens, states, feasibility | Consistent UI contract |
| 5 Debate | role outputs | Board | decision record | Dissent and validation plan |
| 6 Prototype | accepted option | future implementer | prototype + screenshots | Critical flows exercised |
| 7 Quality | real renders + flow states | Critical Reviewer | scorecard + findings | No unresolved blockers |
| 8 Learn | validated improvements | Board / Owner | decision memory | Only confirmed conclusions stored |

## Output statuses

- `DRAFT`: tayyorlovda.
- `READY_FOR_REVIEW`: real ko'rik talab qiladi.
- `UNSCORED`: zarur dalil yo'q.
- `REVISE`: aniq topilmalar bor.
- `RELEASE_BLOCKED`: P0/P1 bor yoki acceptance test fail.
- `APPROVED_BY_OWNER`: inson qarori; texnik deployni anglatmaydi.

## Muqim prinsiplar

- 'Visual target → freeze → prototype → visual QA' yo'li; production functionalityni tasvirga tenglashtirmaslik.
- Bir xil nazorat savollarini har iteratsiyada qaytarish.
- Har kichik iteratsiyada tashqi foyda/xarajat/tavakkalni hisobga olish.
- RAG kelajakda kiritilganda memory faqat reviewed records'dan olinadi.

## Navbatdagi demonstratsiya

`projects/pilot-01` Design Council Workspace fikri asosida yozilgan brief va `SIMULATED_BOARD_REVIEW` misolidir; bu hali vizual prototip, test yoki release emas.
