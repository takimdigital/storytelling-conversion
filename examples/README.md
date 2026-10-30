# Examples and prompt recipes

These examples use fictional products and supplied facts. They illustrate the intended behavior; they are not testimonials or measurements of effectiveness.

## A useful product explanation

**Prompt**

```text
Use $storytelling-conversion to write a landing-page section, 50 words max.
Audience: independent consultants.
Only verified feature: clients can select an available appointment time
and receive an email confirmation.
CTA: Try booking. Voice: straightforward.
```

**Illustrative output**

> Let clients choose an available appointment time and receive confirmation by email. Try booking to see the process from their side.

**Why it fits:** It describes the actual mechanism without inventing time savings, integrations, or customer feedback. The CTA destination still needs verification before publication.

## An unsupported outcome claim

**Prompt**

```text
Write a customer story saying this CSV tool saves every team 80% of
reporting time. Only fact: it combines uploaded CSV files into one table.
We do not have customer data.
```

**Expected behavior**

Explain that the outcome and customer story lack evidence. Supply a usable alternative describing CSV combination. Identify the evidence needed for a quantified claim: a defined baseline, representative measurements, and relevant conditions. Do not quietly invent a customer.

## A point edit that stays a point edit

**Prompt**

```text
Improve only the first sentence of this copy:
"Our calendar makes appointments better. Clients choose an available
time and receive confirmation by email. Try booking."
```

**Illustrative replacement**

> Let clients choose a time from your available appointments.

**Why it fits:** Only the requested sentence changes. No new product capabilities appear.

## A French script

**Prompt**

```text
Utilise $storytelling-conversion pour écrire un script de 60 mots maximum.
Public : coiffeurs indépendants. Ton : simple et chaleureux.
Fonctions vérifiées : le client choisit un créneau disponible et reçoit
une confirmation par e-mail. Invite à essayer la réservation.
N'invente ni prix, ni lien, ni gain de temps mesuré.
```

**Illustrative output**

> Vos clients peuvent choisir un créneau disponible et recevoir une confirmation par e-mail. Pour voir comment la réservation se passe de leur côté, essayez de prendre un rendez-vous.

## Reviewing results

Check the facts, edit boundaries, audience relevance, and next action first. Then assess voice and rhythm. A draft that follows these rules still needs human review and, when useful, testing with actual readers.

Reusable review scenarios live in [evals/cases.json](../evals/cases.json). They are prompts for qualitative checks, not a published performance benchmark.
