---
title: "Email & Aliases: The Complete Privacy System"
description: "Build a Proton Family vault with unlimited aliases, a portable custom domain, a 4-tier alias strategy, and the daily habits that keep it working. Answers the common objections and walks through every step."
topic: "privacy"
category: "identity"
tags: [proton, simplelogin, custom-domain, aliases, encryption, firefox, containers, bazzell]
lastUpdated: 2026-04-23
sidebar:
  order: 20
---

**One inbox to rule them all.**

Your email address is the skeleton key to your entire digital life. Every account you've ever made is tied to it. Data brokers have it. Breached databases have it. When one service leaks it, everything connected to that address is compromised. The system you're about to build makes that impossible.

This guide combines the full technical setup (Proton Family + SimpleLogin + custom domain + Firefox hardening) with the reasoning behind every decision — so you understand what you're building *and* why the common objections to aliases don't hold up.

## Part 1 — Why aliases, really

Before the technical steps, it's worth addressing the three objections that keep most people from ever starting. If you already know why you want this, skip to Part 2.

### "My multiple Google accounts are good enough"

> "I have separate Google accounts for work, personal, and shopping. That's basically the same thing as aliases."

Google knows every one of those accounts is YOU. Same phone, same IP, same device fingerprint, same recovery email. Google's entire business is connecting the dots — they linked your accounts together on Day 1.

Google doesn't need you to tell them the accounts are connected. When you log into your "shopping" Gmail and your "personal" Gmail from the same phone, they see identical device IDs, identical IP addresses, and identical behavioral patterns. Internally, they've built a single advertising profile across all of them. Three Google accounts isn't compartmentalization — it's **three front doors to the same house**.

With Proton aliases, each service gets a **completely different email address** that routes to one encrypted inbox. Amazon has one address. Your doctor has another. Your gym has a third. None of these addresses share a domain with each other (if you use SimpleLogin), and none of them point back to your real inbox. If Amazon gets breached, the attacker finds one dead alias — not your email, not your bank, not your doctor.

:::tip[The actual difference]
Multiple Google accounts = Google sees everything across all of them, and any breach exposes a real email tied to your phone number and identity.

Proton + unique aliases = Each service gets a disposable, killable address. Your real inbox is invisible. One breach = one dead alias. Google sees nothing.
:::

### "I can't act like a robot — fingerprinting means they'll track me no matter what"

You're confusing two different threats. Fingerprinting tracks your BROWSER. Aliases protect your IDENTITY. They solve completely different problems, and you don't need to beat fingerprinting to benefit enormously from aliases.

**Without aliases:** A data broker buys a breached database from LinkedIn. Your real email `jane.doe@gmail.com` is in it. They search that email across every other breached database. They find it on Adobe, Dropbox, MyFitnessPal, and your insurance portal. Now they have your name, address, phone number, passwords, health data, and shopping habits — all tied together by one email address.

**With aliases:** LinkedIn was breached. The address on file is `linkedin-x9k2@simplelogin.co`. The attacker searches every database for that address. They find... nothing. Because no other service has ever seen that alias. The breach is contained to a single dead-end address that you disable with one click.

:::tip[You don't need to beat fingerprinting]
Aliases protect against **data breaches, cross-service tracking by email, and identity correlation** — which are far more common and damaging threats than browser fingerprinting. You don't need to act like a robot. You just need to stop giving every website the same skeleton key to your entire digital life.
:::

### "Google will always have my data even with a Proton alias"

Google gets the data you give THAT service. The point is they can't connect it to everything else you do.

**Google doesn't get to be the hub of your entire identity anymore.** Right now, Gmail is the recovery email for your bank, your medical portal, your insurance, your social media, and every shopping account. Google sees every confirmation email, every password reset, every receipt. They know where you bank, who your doctor is, what you buy, and when you travel.

With aliases: Google gets nothing from your bank (that's a direct Proton alias). Google gets nothing from your doctor (that's your custom domain catch-all). Google gets nothing from Amazon (that's a SimpleLogin alias). Google still has your YouTube data — but that's ALL they have. You went from giving Google access to your **entire life** to giving them access to **one service**.

:::note[The simple analogy]
Using one email everywhere is like using the same key for your house, car, office, and safe deposit box. If someone copies that key once, they have access to everything. Aliases give each door its own unique key. Losing one key loses one door — not your whole life.
:::

## Part 2 — The architecture

```
Amazon            ──→  amazon@quietmail.net    ──→  SimpleLogin catches it  ──→  🔒 Secret Proton Inbox
Bank of America   ──→  boa@quietmail.net       ──→  SimpleLogin catches it  ──→  🔒 Secret Proton Inbox
Random newsletter ──→  news7@quietmail.net     ──→  SimpleLogin catches it  ──→  🔒 Secret Proton Inbox
```

Three layers. The outside world only ever touches the outermost one. Your real inbox is the vault nobody knows about.

| ✗ BEFORE: `jane.doe@gmail.com` | ✓ AFTER: `random8472@proton.me` (secret vault) |
|---|---|
| → Given to every website & person | → Given to NOBODY, ever |
| → Links all your accounts together | → Every service gets a unique alias |
| → Google reads every email | → Proton can't read your email (zero-knowledge) |
| → Data brokers have it | → Brokers can't connect the dots |
| → One breach = everything exposed | → One breach = one dead alias, nothing else |
| → Can't change it without losing everything | → Kill any alias instantly, make a new one |

:::tip[Why Proton specifically?]
ProtonMail is hosted in Switzerland with zero-knowledge encryption. This means your email is encrypted on your device before it's stored on their servers. Even with a court order, Proton employees cannot view your messages. If Proton gets breached, the attacker gets encrypted data that's useless to them. Compare this to Gmail, where Google has full access to every message and has been caught allowing third-party developers to read user emails.
:::

## Part 3 — Create your secret Proton account

This is YOUR primary account — the vault. It must have zero connection to your real identity. Other users on the Family plan will get their own accounts later. You set up the admin account first.

### Step 1 — Turn on your VPN first

Before you open Proton's website, connect to a VPN. This hides your real IP address from Proton when you create the account. ProtonVPN (paid tier) or Mullvad are the recommended options. If you don't have a VPN yet, you can use ProtonVPN's free tier temporarily — it's better than nothing.

:::note[Why]
Your IP address is like your home's fingerprint on the internet. Your ISP assigns it to you, and it can be traced back to your name and address. Without a VPN, Proton logs this IP at signup, creating a link between this "anonymous" account and your real identity.
:::

### Step 2 — Pick a meaningless username

Go to proton.me and create a new account. Choose a username that has absolutely nothing to do with you — no name, no birthday, no city, no pet's name. Think random: `cold.harbor.4491`, `silver.plate.88`, or just random characters. You will never give this address to anyone, ever. Memorize it or store it in a password manager.

:::note[Why]
This address is your vault. It needs to be unguessable and unconnectable to any identity. Think of it like a PIN — you know it, but it's never written on the card. If anyone ever discovers this address, your entire alias system is compromised.
:::

### Step 3 — Use zero real information

When prompted for a display name, use anything fake. **Do not add a recovery phone number** — skip it. **Do not add a recovery email** — skip it. If Proton demands phone verification and you can't bypass it, use a VOIP number (Google Voice on a clean Google account, or a prepaid SIM bought with cash). Write down your password and store it offline in a safe place until you have a password manager set up.

:::note[Why]
Recovery info is a backdoor. Any phone number or backup email tied to this account can be used to identify you, social-engineer access to the account, or unravel your entire privacy setup. No recovery info means no backdoor.
:::

### Step 4 — Enable Two-Factor Authentication (2FA)

Go to Settings → Security → enable 2FA. Use an authenticator app — **Aegis** (Android) or **2FAS** (iPhone) — never SMS. Write your backup codes on paper and store them somewhere physically secure (not on your phone or computer).

:::note[Why]
SMS-based 2FA can be defeated by SIM-swap attacks, where a criminal convinces your phone carrier to transfer your number to their device. An authenticator app generates codes locally on your device — no phone carrier involved, no interception possible.
:::

### Step 5 — Harden your Proton settings

While you're in settings, apply these changes immediately:

```
Settings → Account → Load Embedded Images → Manual
Settings → Account → Request Link Confirmation → Enabled
Settings → Account → Automatically Save Contacts → Disabled
```

:::note[Why]
Embedded images often contain tracking pixels — tiny invisible images that report your IP address, device info, and the exact time you opened an email. Link confirmation prevents accidental clicks on phishing links. Auto-contact storage creates a list of everyone you've ever emailed — evidence you don't need sitting around.
:::

## Part 4 — Upgrade to Proton Family

Proton Family covers up to 6 users. Each person gets their own fully encrypted Proton account with email, calendar, cloud storage, VPN, password manager, and unlimited SimpleLogin aliases. You're the admin — you manage the plan and invite other users.

### Step 1 — Purchase Proton Family

From your new secret account, go to Settings → Subscription → upgrade to **Proton Family**. Choose yearly billing to save. The plan includes 3TB of shared storage, Proton Mail, Calendar, Drive, VPN, Pass (password manager), and SimpleLogin Premium for every user.

For payment, the most private option is a prepaid debit card bought with cash, or Proton credits purchased with Bitcoin. A regular credit card works too — this is a privacy tool, not a crime, and having a payment trail to Proton is not the threat you're worried about.

:::note[Why]
Bazzell notes that he pays for ProtonMail with a credit card in his true name because his email will be associated with his identity eventually anyway, and he doesn't want to risk losing access to the account. The real privacy comes from the alias system, not from hiding the fact that you use Proton.
:::

### Step 2 — Create accounts for other users

From your admin dashboard, invite each user on the plan. They each need to create their own Proton account with their own credentials. You do NOT need to know their passwords. Each person gets their own inbox, their own aliases, their own VPN access — completely separate from yours.

For less tech-savvy users, you may want to sit with them during setup. Help them pick a meaningless username and enable 2FA. Make sure they write down their credentials on paper.

### Step 3 — Set up each user's SimpleLogin

Each user on the Family plan gets SimpleLogin Premium included. Have each user go to the SimpleLogin app or simplelogin.io and sign in with their Proton credentials. Their Proton email becomes the forwarding destination — all aliases route to their own inbox.

:::note[Why]
SimpleLogin is the shield between the world and your real inbox. Websites, companies, and services only ever see a SimpleLogin alias. Your real Proton address stays invisible. If an alias gets compromised, you kill it and make a new one. Your real inbox is untouched.
:::

### Roles on the plan

**👤 YOU (ADMIN)**
: Secret Proton account. Manages the Family plan. Full SimpleLogin with custom domain. All aliases for your services route here.

**Other users**
: Own Proton account. Own SimpleLogin aliases. More tech-savvy users can set up their own custom domains if they want. Up to 6 total users on the plan. For less technical users, you may want to help them migrate old Gmail/Yahoo accounts over time — start with banks and medical.

**Shared-account handling**
: If two users share accounts (joint bank, utilities), create shared aliases that forward to both inboxes.

:::danger[Critical rule for Family setup]
Every user's secret Proton address must stay secret — even from each other. If another user on the plan needs to email you, they email your alias, not your vault address. If they give their email to a doctor's office, they give an alias. The vault address goes nowhere. No exceptions, even within the plan.
:::

## Part 5 — Set up your custom domain

This is the power move. A custom domain means you own the front door. If Proton or SimpleLogin ever disappear, you just point your domain somewhere else and all your aliases keep working. You're never locked in to any provider. Bazzell calls this the strongest piece of the email strategy.

### Step 1 — Choose a domain name

Pick something generic and forgettable. Three rules from the book:

**Never use your name.** A domain like `michaelbazzell.com` gives away your identity the moment anyone sees the email. If you use an alias name for a purchase, `bob.smith@michaelbazzell.com` raises immediate suspicion.

**Keep it generic.** Something that could belong to anyone. Domains with "mail" in them work well. Think `quietmail.net`, `relaybox.org`, `mailvault.io`.

**Avoid privacy-themed names.** `encrypted-secret-mail.com` looks suspicious on a bank application or online purchase. Boring is better.

### Step 2 — Register the domain

Go to **Porkbun** (porkbun.com) or **Namecheap** (namecheap.com). Create an account. Search for your chosen domain name. Most .com/.net domains are $8–15/year. At checkout, make sure **WHOIS privacy** is enabled — this hides your registration details from public view. Both Porkbun and Namecheap include this for free.

For registration info, you need to provide a name and address (ICANN rules). Use your real first initial + last name and your PMB address. Bazzell recommends keeping your real name on the registration so you can prove ownership if challenged — the WHOIS privacy hides it from public view anyway.

:::note[Why]
If you use a completely fake name and ICANN audits the registration, you could lose the domain. Worse, someone else could buy it and impersonate you with real-looking email addresses. Your PMB address keeps you honest without revealing your home.
:::

### Step 3 — Connect the domain to Proton

In Proton: go to `Settings → Domains → Add Custom Domain` and enter your domain name. Proton will give you a set of DNS records to add. In your domain registrar (Porkbun/Namecheap): go to `DNS Settings` or `Advanced DNS` and add the records Proton tells you to.

| Record Type | Purpose | What to Do |
|---|---|---|
| **TXT** | Verify you own the domain | Copy Proton's verification string into a TXT record with host "@" |
| **MX** | Route emails to Proton's servers | Add 2 MX records with the values Proton provides (mail.protonmail.ch, mailsec.protonmail.ch) |
| **TXT (SPF)** | Prevent email spoofing | Add the SPF record Proton provides — this tells other servers only Proton can send email from your domain |
| **CNAME (DKIM)** | Verify emails are authentic | Add 3 CNAME records Proton provides — this cryptographically signs your outgoing emails |

Don't panic if this looks technical — Proton walks you through each record step by step. The whole process takes about 15 minutes. DNS changes can take up to an hour to propagate, but usually it's faster.

### Step 4 — Create your email address & enable catch-all

Once Proton verifies the domain, create at least one address like `hello@quietmail.net`. Then enable the **Catch-All** option next to your domain. This is the magic: any email sent to ANY address @quietmail.net will land in your inbox — even addresses that don't technically exist yet.

This means you can give out `amazon@quietmail.net` to Amazon, `doctor@quietmail.net` to your doctor, `totally.fake.name@quietmail.net` to a sketchy website — and they ALL arrive in your inbox without you needing to set each one up in advance.

:::note[Why]
Catch-all gives you unlimited addresses on the fly. No need to log into SimpleLogin to create an alias first. Just invent an address on the spot. This is what Bazzell uses for over 90% of his communications.
:::

### Step 5 — Connect the domain to SimpleLogin too

You can also add the same domain (or a second domain) to SimpleLogin. This gives you the best of both worlds: Proton's catch-all for quick on-the-fly addresses, and SimpleLogin's management dashboard for organizing, disabling, and monitoring your aliases. In SimpleLogin: go to `Settings → Custom Domains → Add Domain` and follow the DNS setup (similar to Proton's process).

:::note[Why]
SimpleLogin gives you a dashboard to see which aliases are active, how much mail each one gets, and the ability to instantly disable any alias that starts getting spam. Catch-all gives you convenience; SimpleLogin gives you control.
:::

## Part 6 — The 4-tier alias strategy

This is where most guides stop at "just make aliases." Here's the actual system — how to organize them, when to use catch-all vs. SimpleLogin, and how to handle different risk levels.

### Tier 1 — Critical accounts (use Proton aliases directly)

For banking, brokerage, and financial accounts — **do NOT use SimpleLogin or your custom domain**. Use a Proton alias address directly (Proton Family gives you 15 aliases per user). Why? If SimpleLogin or your domain registrar ever goes down, you lose access to your bank. Proton aliases live inside Proton itself — no middleman.

Example: `finances7722@proton.me` — used for your bank, credit cards, brokerage accounts only. Generic name, no identity attached, but hosted directly by Proton with no third-party dependency.

:::note[Why]
Bazzell is explicit: "NEVER use a forwarding or masking email service for anything vital. If these services would disappear tomorrow, you would lose access to the accounts." Your bank account is not worth the risk of relying on a middleman.
:::

### Tier 2 — Important accounts (use custom domain catch-all)

For medical, insurance, government services, and important personal accounts, use your custom domain catch-all. These are important but not catastrophic if there's a brief disruption. If your domain registrar has issues, you can transfer the domain to another registrar and keep all your addresses.

Examples: `doctor@quietmail.net`, `insurance@quietmail.net`, `dmv@quietmail.net`

:::note[Why]
You own the domain. If Proton disappears, you point the domain to a new email provider. If Namecheap disappears, you transfer the domain to Porkbun. The addresses are portable — they follow you no matter what happens to any single company.
:::

### Tier 3 — Everything else (use SimpleLogin aliases)

For shopping, subscriptions, newsletters, forums, random websites, loyalty programs, and anything disposable — use SimpleLogin. These are the accounts most likely to spam you, sell your data, or get breached. SimpleLogin makes it trivial to kill an alias the moment it becomes a problem.

Examples: `amazon-xk92@simplelogin.co`, `netflix-4m7p@simplelogin.co`, `newsletter-junk@simplelogin.co`

:::note[Why]
If Amazon gets breached and your alias starts getting phishing emails, you disable the alias in one click. Make a new one. Update your Amazon account. The breach is contained to that single alias — nothing else in your life is affected.
:::

### Tier 4 — Data removal & opt-outs (use a dedicated alias)

When you send CCPA demand letters or submit data broker opt-out requests, many of them require an email address. **Never use your real Proton address for this.** Create a dedicated SimpleLogin alias like `removals@simplelogin.co` specifically for privacy removal requests. If a broker starts spamming this address or sells it, kill it and make a new one.

:::note[Why]
Some data broker removal sites are actively hostile to privacy-seekers. At least one site publicly displayed the names of everyone who requested removal using a disposable email address. Using a dedicated alias contains this risk to a single throwaway address.
:::

### Your complete alias architecture

```
TIER 1 — Banks            →  Proton alias directly          (no middleman)
TIER 2 — Medical/Gov      →  Custom domain catch-all        (you own the domain)
TIER 3 — Shopping/Junk    →  SimpleLogin aliases            (disposable & killable)
TIER 4 — Removals         →  Dedicated throwaway alias      (expect hostility)
```

### Quick reference: which alias when?

| Situation | What to Use | Why |
|---|---|---|
| **Banks, credit cards, brokerage** | Direct Proton alias<br>`finances7722@proton.me` | No middleman. If SimpleLogin disappears, your bank email still works |
| **Doctor, insurance, government** | Custom domain catch-all<br>`doctor@quietmail.net` | You own the domain. Portable if Proton disappears. Just invent it on the spot |
| **Shopping, subscriptions, apps** | SimpleLogin alias<br>`amazon-k9x@simplelogin.co` | Killable. If it gets spam, disable it in one click and make a new one |
| **Junk signups, sketchy sites** | SimpleLogin random alias | Disposable. No thought required. If compromised, who cares |
| **Data broker removal requests** | Dedicated throwaway alias<br>`removals@simplelogin.co` | Some brokers are hostile. Isolate this activity completely |

### The catch-all trick (your daily superpower)

Once catch-all is enabled on your custom domain, you can **invent email addresses on the fly**. Standing at a store checkout and they want an email? Say `storename@quietmail.net`. Signing up for a newsletter? Type `newsletter7@quietmail.net`. You don't need to pre-create anything — every address @quietmail.net automatically arrives in your inbox.

:::danger[The one rule everyone must follow]
**Your real Proton vault address goes NOWHERE. Ever.** Not on any website, not on any form, not even between users on the same plan. Your vault address is the lock on the safe — it never leaves the safe. If anyone ever discovers it, your entire system is compromised.
:::

## Part 7 — Browser setup (Firefox)

This isn't about acting like a robot. It's about making Firefox do the heavy lifting for you — blocking trackers, isolating accounts, and stopping scripts that spy on you. Once set up, you browse normally. The browser handles the rest.

:::tip[Already using LibreWolf?]
If you've gone through the [LibreWolf Hardening guide](/privacy/browsers/librewolf-hardening/), most of this Part is already done for you — LibreWolf ships with hardened defaults, uBlock Origin pre-installed, and tracking protection enabled. Skip to the Multi-Account Containers section. This Part exists for users who aren't ready to switch to LibreWolf yet and want to harden regular Firefox instead.
:::

### Step 1: Switch to Firefox

Chrome is made by Google. It is literally built to track you. Safari is better but limited. Firefox is open source, respects privacy by default, and supports the tools that make aliases work seamlessly. Download it from **mozilla.org/firefox** on every device.

### Step 2: Harden Firefox settings (5 minutes per device)

Open Firefox → click the menu (☰) → Settings. Apply these changes:

- **General:** Uncheck "Recommend extensions" and "Recommend features"
- **Home:** Set homepage and new tabs to "Blank Page." Disable all Home Content
- **Search:** Change default search to **DuckDuckGo**. Uncheck all "Provide search suggestions"
- **Privacy & Security:** Select **"Strict"** protection
- Check "Delete cookies and site data when Firefox is closed"
- Uncheck "Show alerts about passwords for breached websites"
- Uncheck all "Suggest and generate" and "Autofill" password options
- History → "Firefox will use custom settings" → Uncheck "Remember browsing history" and "Remember search and form history" → Check "Clear history when Firefox closes"
- Permissions → Block new requests for Location, Camera, Notifications
- Uncheck everything under "Firefox Data Collection and Use"
- Enable "HTTPS-Only Mode in all windows"

:::note[Why]
These settings stop Firefox from sharing your browsing data, prevent sites from auto-requesting your location, and ensure cookies are wiped every session. The "Strict" protection enables Total Cookie Protection — Firefox isolates cookies per-site, so Amazon can't see your Facebook cookies.
:::

### Step 3: Install two essential extensions

**uBlock Origin — your invisible shield**

Install from `addons.mozilla.org/firefox/addon/ublock-origin`

This single extension replaces AdBlock, Privacy Badger, NoScript, and Disconnect. It blocks ads, tracking scripts, malicious code, and fingerprinting scripts — all automatically. After install:

- Click the uBlock icon → Dashboard (gear icon) → Settings → check **"I am an advanced user"**
- Go to Filter Lists tab → under Privacy, enable **"Block outsider intrusion into LAN"** and **"AdGuard Base"**
- Click "Apply Changes" then "Update Now"

:::note[Why]
uBlock Origin blocks the tracking scripts that fingerprint your browser. It won't make you invisible, but it eliminates the vast majority of third-party trackers. CNN alone loads dozens of tracking scripts from Twitter, Amazon, and ad networks — uBlock blocks them all silently. You won't even notice it's there, except that pages load faster.
:::

**Multi-Account Containers — your alias powerhouse**

Install from `addons.mozilla.org/addon/multi-account-containers`

This is the extension that makes aliases practical. Containers are like separate browsers inside one browser — each with its own cookies, logins, and sessions. Create these containers:

- 🔴 **Google** — Force all Google sites to open here. This traps Google tracking inside one container.
- 🔵 **Banking** — Open your bank, credit cards, and financial sites here.
- 🟢 **Shopping** — Amazon, stores, and purchases.
- 🟣 **Social** — Facebook, Instagram, Reddit.
- 🟡 **General** — Everything else.

:::note[Why]
Without containers, when you browse Amazon and then open Facebook, Facebook's tracking scripts can see your Amazon cookies. With containers, Facebook is sealed off — it can't see what's happening in Shopping or Banking. Each container is a separate world. This is the answer to "I can't act like a robot." You're not changing your behavior. The container does the isolation for you.
:::

### Step 4: Force Google into its container

After creating the Google container:

- Open a new Google container tab → go to **google.com**
- Click the Containers menu → select **"Always open this site in Google"**
- Navigate to google.com from a normal tab → select **"Remember my decision"** → click "Open in Google"

Now any time you visit Google, Gmail, YouTube, or any Google property, it opens in the Google container automatically. Google's tracking is sealed off from the rest of your browsing. **You change nothing about how you browse.** Firefox does the containment for you.

### Step 5: Set up DNS-level protection (optional but powerful)

Create a free account at **nextdns.io**. Enable their recommended blocklists. Then in Firefox:

- Settings → scroll to Network Settings → click Settings
- Check "Enable DNS over HTTPS" → select Custom
- Enter your NextDNS address: `https://dns.nextdns.io/YOUR-ID`

Then go to `about:config` in the URL bar → search for `network.trr.mode` → change to **3**.

:::note[Why]
This adds a second layer of tracking protection at the DNS level — even if a tracker somehow slips past uBlock Origin, NextDNS blocks it before the connection happens. It also encrypts your DNS queries so your ISP can't see what sites you visit. Each user can customize their own blocking preferences without affecting anyone else.
:::

## Part 8 — Migrate everything over

This is the slow, painful, but most important part. Every account you have that uses your old email needs to be moved to the new system. Don't try to do this in one sitting — spread it over a few weeks. Start with the highest-risk accounts.

### Step 1 — Audit every account you own

Go through your old inbox (Gmail, Yahoo, whatever). Search for keywords like "welcome to", "verify your email", "account created", "receipt", "password reset". Build a list of every service. You will find way more than you expected. Prioritize this order:

1. **Financial** (banks, credit cards, brokerage)
2. **Medical & Insurance**
3. **Government** (SSA, IRS, DMV)
4. **Shopping & subscriptions**
5. **Everything else**

### Step 2 — Update each account to the right alias tier

For each service, go to account settings and change the email address to the appropriate alias from the tier system above. Bank → Proton alias. Doctor → custom domain. Amazon → SimpleLogin alias. **One unique alias per service, always.**

:::note[Why]
One alias per service means one breach = one dead alias. The damage doesn't cascade to everything else. If you reuse an alias across multiple services, a breach at any one of them compromises all of them.
:::

### Step 3 — Forward your old email to Proton (temporarily)

Don't delete your old accounts yet. Set them to forward all incoming mail to your new Proton inbox. This catches anything you missed during migration.

```
Gmail:   Settings → Forwarding and POP/IMAP → Add a Forwarding Address
Yahoo:   Settings → Accounts → Forward
Outlook: Settings → Mail → Forwarding → Start Forwarding
```

:::note[Why]
You'll inevitably miss accounts during migration. Forwarding catches stray emails so nothing falls through the cracks. Once you've gone a few months with no forwarded emails arriving, you know you've caught everything.
:::

### Step 4 — Delete old accounts (don't just abandon)

Once you're confident everything is migrated and no forwarded emails have arrived for at least a month, **delete** the old Gmail/Yahoo/etc. accounts entirely. Don't just stop using them — actually delete them. Abandoned accounts can still be exploited for password resets, data requests, or social engineering.

:::note[Why]
An abandoned Gmail account with your name on it is a liability. If someone gains access to it (through a breach, social engineering, or password reuse), they can use it to reset passwords on any account still linked to that address. Deletion is the only clean break.
:::

### Step 5 — Help other users on your plan migrate too

Other users on your Family plan need to go through the same process. This will take longer for users who have decades of accounts. Start with their highest-risk accounts (banking, medical) and handle the rest gradually. You don't need to do it all at once — even migrating their top 10 accounts provides massive improvement.

## Part 9 — The habits that make it stick

Setup is one-time. These habits are permanent. They're what actually keep you invisible after everything is configured.

🔒 **Your real Proton address is a secret.** It goes nowhere — no websites, no forms, no "just email me at...". Not even to other users on your plan. If someone wants to email you, they email an alias. The vault address is for receiving forwarded mail from aliases only. Ever.

📧 **Always reply through the alias.** When you reply to an email in Proton, make sure the "From" field shows the alias or custom domain address — not your real vault address. Proton lets you choose which address to send from. Double-check every time.

🎯 **One alias per service, always.** Amazon gets one alias. Your gym gets a different one. Your doctor gets another. Never combine or reuse. If you run out of SimpleLogin free aliases, the paid tier (included in Family) gives you unlimited.

🔥 **Spam = instant investigation.** If an alias starts getting spam, find out why. Did that company get breached? Did they sell your data? Kill the alias, make a new one, update the account. The breach is now contained. This is the system working as designed.

🌐 **Always use VPN when accessing Proton.** Your home IP logging into your vault address is a breadcrumb. Proton Family includes ProtonVPN for every user — there's no excuse. VPN on, then open Proton. Every time.

🛡️ **Never link Proton to your identity.** No "Sign in with Google." No importing contacts from other services. No linking social media accounts. No using the same password as any other service. Proton is an island.

📸 **Keep tracking pixels blocked.** Proton blocks remote images by default — you set this in Part 3. Never turn it back on. Those invisible images tell senders your IP address, what device you're on, and the exact second you opened their email.

📋 **Check your email rules periodically.** A compromised account can have its email silently forwarded to an attacker. Go to Settings → Filters and make sure no unauthorized forwarding rules exist. One documented case involved a client losing $50,000 because a criminal added a forwarding rule to copy all incoming messages.

🧩 **Use containers without thinking about it.** Once Google is set to "Always open in Google container", you literally change nothing. You click links normally. Firefox routes things automatically. Shopping goes to Shopping. Banking goes to Banking. You just browse.

## For the user who still isn't convinced

Fair enough. Here's the absolute minimum that costs zero effort after initial setup.

**Even if you change nothing else, do these three things:**

1. **Use your Proton inbox instead of Gmail.** Your email is now encrypted. Google can't read it. Hackers who breach Proton get useless encrypted data. You don't need to delete Gmail yet — just forward it to Proton and start using Proton as your daily inbox.

2. **Install uBlock Origin on Firefox.** It runs silently and blocks tracking scripts everywhere you go. Zero effort after install. Pages load faster. Fewer creepy "how did they know I was looking at that" ads.

3. **Use a catch-all alias for anything new.** Any time you sign up for something going forward, use `whatever@quietmail.net` instead of your Gmail. You don't even need to change old accounts yet — just stop giving out your real email starting today. That alone prevents future breaches from connecting back to you.

:::tip[The pitch that actually works]
You don't need to be invisible. You don't need to act like a robot. You just need to stop handing every website the same master key to your entire digital life. Aliases cost zero dollars, take 10 seconds per signup, and mean that the next data breach — and there WILL be a next one — is a shrug instead of a crisis.
:::

## Your complete action list

### Proton account setup (one-time, ~30 min)

- [ ] Connect to VPN before doing anything — *critical*
- [ ] Create new Proton account with random meaningless username, no real info, no recovery — *critical*
- [ ] Enable 2FA with authenticator app (Aegis / 2FAS), store backup codes on paper — *critical*
- [ ] Harden Proton settings: disable remote images, enable link confirmation, disable auto-contacts — *critical*
- [ ] Upgrade to Proton Family (yearly billing) — *critical*
- [ ] Invite other users and help them create their own Proton accounts — *important*
- [ ] Each user: enable 2FA, harden settings, set up SimpleLogin — *important*

### Custom domain setup (one-time, ~30 min)

- [ ] Register a generic custom domain at Porkbun or Namecheap with WHOIS privacy — *important*
- [ ] Add custom domain to Proton: configure TXT, MX, SPF, and DKIM records — *important*
- [ ] Enable catch-all on your custom domain — *important*
- [ ] Optionally connect custom domain to SimpleLogin for alias management — *optional*

### Alias system (one-time, ~10 min)

- [ ] Set up Proton aliases (not SimpleLogin) for Tier 1 financial accounts — *critical*
- [ ] Create dedicated removal alias for data broker opt-outs (Tier 4) — *important*
- [ ] Understand the tier system: Banks→Proton alias, Medical→catch-all, Shopping→SimpleLogin — *critical*

### Browser setup (one-time, ~15 min per device)

- [ ] Install Firefox (or LibreWolf), hide Chrome/Safari/Edge — *important*
- [ ] Harden Firefox settings (Strict protection, clear on close, HTTPS-only, DuckDuckGo) — *important*
- [ ] Install uBlock Origin — enable advanced user, AdGuard filter, LAN intrusion blocking — *important*
- [ ] Install Multi-Account Containers — create Google, Banking, Shopping, Social, General — *important*
- [ ] Set Google to "Always open in Google container" — *important*
- [ ] Optional: Set up NextDNS in Firefox (DNS over HTTPS, mode 3) — *optional*

### Migration (gradual, over weeks)

- [ ] Audit old email inbox — list every account ever created — *critical*
- [ ] Migrate financial accounts to Proton aliases (Tier 1) — *critical*
- [ ] Migrate medical & insurance accounts to custom domain (Tier 2) — *critical*
- [ ] Migrate shopping & subscriptions to SimpleLogin aliases (Tier 3) — *important*
- [ ] Set old email accounts to forward to Proton — *important*
- [ ] Help other users migrate their top 10 highest-risk accounts — *important*
- [ ] After 1+ month with no forwarded stragglers: delete old email accounts entirely — *critical*

### Ongoing habits (daily, forever)

- [ ] Every new signup: unique alias (catch-all or SimpleLogin)
- [ ] Never give vault address to anyone or any site
- [ ] Check "From" field before sending replies
- [ ] Spam on an alias? Disable it, investigate, make a new one
- [ ] Use containers without thinking about it
- [ ] VPN on before accessing Proton

---

*Based on guidance from* Extreme Privacy *by Michael Bazzell and* OSINT Techniques *by Bazzell & Edison.*

**The goal isn't perfection — it's making breaches boring instead of catastrophic.**
