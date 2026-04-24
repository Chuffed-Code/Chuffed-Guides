---
title: "The Privacy Roadmap — Master Sequencing Guide"
description: "Every privacy guide connected in the correct order — PMB, Proton, Optery, phone stack, payments. What to do first, what to pay with, and why the sequence matters."
topic: "privacy"
category: "roadmap"
tags: [roadmap, sequencing, pmb, proton, optery, privacy-com]
lastUpdated: 2026-04-23
sidebar:
  order: 0
---

**The Master Sequencing Guide**

Every guide you've built — PMB, Proton, Optery, phone numbers, payments — connected in the correct order. What to do first, what to pay with, and why the sequence matters.

## Why it feels like you need *everything* to start *anything*

You want to sign up for Proton, but you need a private payment method. You want Privacy.com, but you need an email and an address. You want a PMB, but you need... a credit card? It feels circular. But it's not — because **not everything needs to be private from the start.**

:::caution[The trap]
Thinking you need perfect privacy at every step before you can take the first step. This is paralysis. You will never start.
:::

:::tip[The reality]
Some services are **designed to know who you are**. Your PMB needs your real name — that's the whole point. Proton can have your real credit card — the privacy comes from the alias system, not from hiding that you pay for it. You build privacy in layers, and the first layer is laid with your regular identity. Each subsequent layer uses the infrastructure from the one before it.
:::

### The dependency chain — what enables what

```
VPN → Proton Account → SimpleLogin Aliases
PMB Ghost Address → Privacy.com → Custom Domain
Aliases + PMB + Privacy.com → Optery → Phone Stack
```

**Payment legend:**
- 🟡 Regular card OK
- 🟣 Use Privacy.com
- 🟢 Cash
- 🟠 Crypto
- 🔵 Free

## Every step, *in order*

### Day 1 — The Bootstrap: VPN + Proton

**01. Get a VPN** — *Cash or Crypto*

Go to **mullvad.net**. No email needed, no name needed — it just generates an account number. Pay with cash (mailed in an envelope) or crypto for maximum privacy. Or use ProtonVPN's free tier temporarily if you need to start right now.

:::note[WHY FIRST]
Everything you do after this should be behind a VPN. Your IP address is a fingerprint that links your real identity to every account you create. VPN on = fingerprint gone. This is step zero.
:::

**02. Create your secret Proton account** — *Free*

VPN on. Go to proton.me. Create account with a **random meaningless username**. No real name, no recovery email, no recovery phone. Enable 2FA with an authenticator app. Harden settings (disable remote images, auto-contacts, enable link confirmation). This is your vault — you will never give this address to anyone.

**Requires:** Nothing. Just a VPN connection and a browser.

**03. Upgrade to Proton Family** — *Regular Card*

From your new account: Settings → Subscription → **Proton Family** (yearly billing). Pay with your regular credit card. Yes, really.

:::note[WHY REGULAR CARD]
Bazzell pays for Proton with his real credit card. The privacy doesn't come from hiding that you use Proton — it comes from the alias system you build on top of it. You also don't want to risk losing access to your email over a failed anonymous payment. This is one of the services that's **okay to have your name on**.
:::

↳ *Proton Family unlocks →* SimpleLogin Premium, ProtonVPN, Proton Pass, Proton Drive for all 6 users

**04. Set up SimpleLogin** — *Included*

Go to simplelogin.io and sign in with your Proton credentials. Create your first few aliases: one for shopping, one for newsletters, one for data broker removals. Each alias forwards to your vault inbox. You now have disposable email addresses.

**05. Invite household members to Proton Family** — *Included*

From your admin dashboard, invite up to 5 other users (6 total on the plan). Help each create their own anonymous Proton account, enable 2FA, and connect SimpleLogin. Each person gets their own inbox, aliases, and VPN.

### Week 1 — Ghost Address: PMB Setup

**06. Set up PMB at Americas Mailbox** — *Regular Card*

Go to americasmailbox.com. Download the Mail Service Agreement. Choose the **Titanium Plus SuperScan Plan**. Fill it out with your **real name** and **real driver's license**. Complete USPS Form 1583 (include a trust name in Box 5). Get it notarized. Submit with your passport as ID and pay with your regular credit card.

:::note[WHY REGULAR CARD + REAL NAME]
This is your ghost address. The entire strategy is to make your real identity point HERE instead of your home. You **want** your name openly linked to this address. Banks, credit bureaus, data brokers — they should all think you live in South Dakota. Hiding your identity from your PMB would defeat the purpose.
:::

**Wait ~1 week** for your welcome packet to arrive with your new PMB address.

**07. Find a local pickup point** — *Cash*

Find an **independent shipping store** a town or two away from your home. Walk in, ask if they'll receive packages for you. Pay the deposit in cash (~$20). No USPS forms, no government paperwork. This is where your PMB forwards mail to — never directly to your home.

**08. Test the PMB chain** — *Free*

Send a test letter to your new PMB. Confirm the scan arrives by email. Request forwarding to your local pickup spot. Confirm you can retrieve it. Full chain works? You're operational.

### Week 2 — Custom Domain + Privacy.com

**09. Register your custom email domain** — *Regular Card*

Go to **Porkbun** or **Namecheap**. Pick a generic, boring domain name (~$10/yr). Enable WHOIS privacy. For the registration address, use your **PMB address** (now live). Use your real first initial + last name so you can prove ownership if ICANN audits you.

↳ *Requires →* PMB address (from Step 06) for registration

**10. Connect domain to Proton + enable catch-all** — *Free*

In Proton: Settings → Domains → Add Custom Domain. Add the DNS records (TXT, MX, SPF, DKIM) in your domain registrar. Enable catch-all. You now have unlimited on-the-fly email addresses at your own domain. Optionally connect the domain to SimpleLogin too for alias management.

**11. Sign up for Privacy.com** — *Free Tier*

Now that you have both a Proton alias AND a PMB address, sign up for Privacy.com. Use a **SimpleLogin alias** as your email (not your vault address). Use your **PMB address** as your physical address. Connect a **dedicated checking account** (not your main one — open a secondary checking account just for Privacy.com).

:::note[WHY NOW AND NOT EARLIER]
Privacy.com requires KYC — they need your real name, DOB, SSN, and a verified physical address. By waiting until your PMB is live, your "physical address" on file with Privacy.com is your ghost address in South Dakota, not your home. Your name is real (required by law), but your address is the PMB. This is the first service where the infrastructure you've built actually pays off.
:::

↳ *Requires →* Proton alias (email), PMB address (physical), bank account

:::tip
**Privacy.com has a $300/week spending limit for new accounts.** Start making small purchases immediately to build history. Over time, limits increase. You can call support to request higher limits once you have a track record. Don't wait until you need it for a big purchase — start small now so it's ready when you need it.
:::

**12. Configure Privacy.com settings** — *Free*

Enable **"Private Payments"** — this hides merchant names from your bank statement. All transactions appear as "Privacy.com" instead of "Amazon" or "Netflix." Enable 2FA. Never use your real home address as a billing address on any Privacy.com card — always use the PMB or a random address.

### Week 3–4 — The Great Migration

**13. Migrate addresses to PMB everywhere** — *Free*

Change your mailing address at every institution — banks, credit cards, brokerage, insurance, subscriptions. Do this **manually, one by one**. Do NOT file a USPS Change of Address form (it feeds data brokers). Within a month, credit bureaus and LexisNexis start showing the SD address instead of your home.

**14. Migrate email accounts using the 4-tier system** — *Free*

Go through your old inbox. For each service, change the email to the appropriate tier:

- **Tier 1 (Banks)** → Proton alias directly (no middleman)
- **Tier 2 (Medical/Gov)** → Custom domain catch-all
- **Tier 3 (Shopping/Junk)** → SimpleLogin alias
- **Tier 4 (Data broker removals)** → Dedicated throwaway alias

**15. Forward old email → delete later** — *Free*

Set your old Gmail/Yahoo/etc. to forward everything to Proton. This catches accounts you missed. After 1+ month with no forwarded stragglers, **delete the old accounts entirely** — don't just abandon them.

**16. Swap payment methods on recurring services**

Now that Privacy.com is active, start replacing your real credit card on online services with Privacy.com masked cards. Create a **merchant-locked card per service** — one for Netflix, one for Amazon, one for Spotify. Use your PMB as the billing address on every card.

**Keep your real AMEX/credit card** for: trusted in-person merchants where you want rewards, and any service that blocks virtual cards. Use Privacy.com for everything else online.

### Month 2 — Nuke the Data Brokers + Credit Freeze

:::tip[Why wait until Month 2?]
You want your PMB address to have propagated through credit bureaus before activating Optery. This way, when brokers re-scrape public records, they find the ghost address — not your home. Optery removes the old listings while the new data flowing in is already clean.
:::

**17. Activate Optery Ultimate** — *Privacy.com Card*

Sign up at optery.com. Start with Free Basic to get your Exposure Report. Then upgrade to **Ultimate (yearly, ~$249)**. Pay with a Privacy.com card — Optery doesn't need to know your real card number. Add all name variations, past cities, emails, and phone numbers. The automated removal begins immediately across 635+ sites.

Set up separate Ultimate accounts for each household member on your plan (~$249 each).

↳ *Requires →* Privacy.com (payment), Proton alias (email), PMB already propagated

**18. Freeze your credit at all three bureaus** — *Free*

Go to Equifax, Experian, and TransUnion websites. Place a **credit freeze** on each. Then add a **fraud alert** at one bureau (it propagates to all three). This prevents new accounts from being opened in your name and adds a phone verification step.

**19. Opt out of pre-screened offers** — *Free*

Go to **optoutprescreen.com** and choose the permanent opt-out. This stops pre-approved credit offers that are commonly stolen from mailboxes and used for identity fraud. Mail the required form to make it permanent.

**20. Hit the big aggregators directly** — *Free*

Even with Optery running, manually submit removals to: **LexisNexis** (optout.lexisnexis.com), **Acxiom**, **Thomson Reuters/CLEAR**, and **TLO/TransUnion**. These backbone databases feed hundreds of smaller sites. Taking them down causes a cascade.

### Month 3+ — Phone Stack + Ongoing Hardening

**21. Set up Silent.link (anonymous carrier eSIM)** — *Bitcoin or Monero*

Go to silent.link (VPN on). Buy the cheapest plan with a US phone number. Pay with Bitcoin or Monero — no name, no address, no identity. Install the eSIM QR code on your phone. This is your carrier-grade number for bank verifications and government services that reject VoIP numbers.

**22. Set up JMP.chat (daily VoIP number)** — *Bitcoin or Card*

Go to jmp.chat. Choose a US/Canadian number. Use your Proton alias as your email. Verify with your **Silent.link number**. Pay with Bitcoin for maximum privacy, or a card if you prefer. Download Cheogram. This becomes your daily phone number for calls, texts, and giving out to businesses.

↳ *Requires →* Silent.link (for verification), Proton alias (email)

**23. Set up SMSPool (disposable verifications)** — *Monero*

Go to smspool.net. Add $5 in Monero. Use this for one-off verifications when signing up for new apps and services (~$0.30 each). Saves your Silent.link number from being burned on throwaway signups.

**24. Help less technical users through a simplified subset** — *Their Cards*

Less technical users on your Family plan don't need the phone stack or custom domain. Focus on getting them through: Proton account + SimpleLogin → PMB address migration → top 10 account email migration → Optery for one year. This alone is a massive improvement.

### Month 13+ — Maintenance Mode — Forever

**25. Downgrade Optery to Free Basic** — *Free*

Before your Ultimate subscription auto-renews, downgrade to Free Basic. You keep quarterly Exposure Reports forever. When re-listings appear, nuke them with CCPA demand letters using the General Delivery address in Los Angeles. About 1 hour of work per quarter. $0/year.

**26. Quarterly CCPA maintenance** — *Free*

Every 3 months: check Optery Free Basic Exposure Report → send CCPA letters to any re-listings → submit Google/Bing re-index requests for removed pages. That's it. Your PMB ensures re-listings only show the ghost address anyway.

## When to use *which payment*

This is the question that trips everyone up. Here's the definitive answer — what to pay with for every service in the roadmap, and why.

| Service | Pay With | Why |
|---|---|---|
| Mullvad VPN | Cash | Mail $5 in an envelope. No identity needed at all. |
| Proton Family | Regular Card | You don't want to lose access. Privacy comes from aliases, not payment. |
| Americas Mailbox PMB | Regular Card | Real name + real card is required and intentional. This IS your ghost address. |
| Custom Domain | Regular Card | ~$10/yr. Use PMB as address. Don't risk losing a domain over anon payment. |
| Privacy.com | Free (bank-funded) | Funded by bank account. Uses PMB as address. KYC required (real name + SSN). |
| Optery Ultimate | Privacy.com | No reason for Optery to have your real card. Masked card + alias email. |
| Silent.link eSIM | Bitcoin / Monero | The whole point is zero identity. Crypto only — no card, no name, no trace. |
| JMP.chat | Bitcoin or Card | Bitcoin preferred. Card acceptable — JMP only has your email alias anyway. |
| SMSPool | Monero | Disposable service, zero identity. Monero for complete anonymity. |
| Online shopping | Privacy.com | Merchant-locked cards. Alias billing name. PMB billing address. |
| Trusted in-person stores | AMEX (opted out) | Keep your rewards. Opt out of all data sharing in AMEX settings. |
| Sensitive purchases | Cash | Medical, legal, anything you wouldn't want in a targeted ad. Cash only. |

:::caution
**Privacy.com is NOT invisible.** It hides merchants from your bank, and hides your real card from merchants. But Privacy.com itself knows your identity (KYC), and a court order can reveal everything. For truly sensitive purchases, cash is the only answer. Privacy.com is for convenience privacy, not adversarial privacy.
:::

## The full sequence, *at a glance*

### Day 1 — The Bootstrap

- [ ] Get VPN (Mullvad with cash, or ProtonVPN free)
- [ ] Create anonymous Proton account (VPN on, random username, no recovery, 2FA)
- [ ] Upgrade to Proton Family — regular card
- [ ] Set up SimpleLogin + create first aliases
- [ ] Invite household members → help them set up Proton + SimpleLogin + 2FA

### Week 1 — Ghost Address

- [ ] Sign up for Americas Mailbox PMB — real name, real card
- [ ] Complete USPS Form 1583 (include trust name in Box 5)
- [ ] Get forms notarized, submit with passport + utility bill
- [ ] Find local independent shipping store as pickup point — cash deposit
- [ ] Test full chain: PMB receives → scans → forwards → you pick up

### Week 2 — Domain + Privacy.com

- [ ] Register custom domain (Porkbun/Namecheap) — PMB address, WHOIS privacy
- [ ] Connect domain to Proton (DNS records) + enable catch-all
- [ ] Sign up for Privacy.com — Proton alias email, PMB address, dedicated checking account
- [ ] Enable Private Payments + 2FA on Privacy.com
- [ ] Start making small Privacy.com purchases to build spending limit

### Week 3–4 — The Great Migration

- [ ] Change mailing address to PMB at all institutions (manually — NO USPS COA form)
- [ ] Migrate financial emails → Proton aliases (Tier 1)
- [ ] Migrate medical/gov emails → custom domain (Tier 2)
- [ ] Migrate shopping/junk emails → SimpleLogin aliases (Tier 3)
- [ ] Replace real cards on online services with Privacy.com merchant-locked cards
- [ ] Forward old email to Proton (temporary safety net)
- [ ] Help other household members migrate their top 10 accounts

### Month 2 — Nuke Data Brokers

- [ ] Activate Optery Ultimate (~$249) — Privacy.com card
- [ ] Activate Optery Ultimate for each other household member (~$249 each)
- [ ] Freeze credit at Equifax, Experian, TransUnion + add fraud alert
- [ ] Opt out permanently at optoutprescreen.com
- [ ] Manually hit LexisNexis, Acxiom, Thomson Reuters, TLO

### Month 3+ — Phone Stack

- [ ] Set up Silent.link eSIM — Bitcoin/Monero only
- [ ] Set up JMP.chat — verify with Silent.link number
- [ ] Set up SMSPool — Monero, for disposable verifications
- [ ] Delete old Gmail/Yahoo accounts entirely (after 1+ month of forwarding)

### Month 13+ — Maintenance (Forever)

- [ ] Downgrade Optery to Free Basic before auto-renewal
- [ ] Every quarter: check Exposure Report → CCPA letters → re-index requests

---

*Based on Extreme Privacy by Michael Bazzell · Connects: PMB Guide · Optery Guide · Email Privacy Guide · Phone Stack Guide · Financial Privacy Guide*
