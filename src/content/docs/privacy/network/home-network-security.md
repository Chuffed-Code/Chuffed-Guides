---
title: "Home Network Security: pfSense + VPN Kill Switch"
description: "Build a hardware firewall that forces every device in your house through a VPN. If the VPN drops, the internet stops — no exceptions, no leaks."
topic: "privacy"
category: "network"
tags: [pfsense, protonvpn, firewall, kill-switch, protectli, bazzell]
lastUpdated: 2026-04-23
sidebar:
  order: 10
---

**The Most Important Chapter in Extreme Privacy**

Every device in your house is broadcasting your real IP address to Apple, Google, Microsoft, Netflix, and your ISP. A pfSense firewall with a permanent VPN fixes this for every device simultaneously — and kills your internet if the VPN ever drops.

**pfSense Firewall · ProtonVPN · Kill Switch · Whole-Home Protection · ~$400 one-time**

## Why a VPN app on your phone isn't enough

You might already have a VPN app on your laptop or phone. That's a good start — but it has a fatal flaw. Every time your device connects to your home Wi-Fi, there are **milliseconds** between getting internet access and the VPN app establishing its secure tunnel. In those milliseconds, your computer sends data to Apple or Microsoft using your **real home IP address**. Your IP gets logged. Your home gets fingerprinted. The VPN connects a moment later, but the damage is done.

And that's just your laptop. What about your smart TV? Your streaming stick? Household members' phones? Tablets? The Ring doorbell? The smart thermostat? **None of these devices run VPN apps.** Every single one is broadcasting your real IP address to its manufacturer's servers 24/7. Your ISP sees all of it. Your ISP sells all of it.

:::note[What your ISP knows right now]
Your home IP address is unique to your house. Your ISP assigns it and can see every connection made from it — which websites, which services, what time, how much data. They sell this to marketing companies. They comply with government requests. And every device manufacturer (Apple, Google, Samsung, Roku, Amazon) stores your home IP and associates it with your account — forever.
:::

The solution is a **hardware firewall** that sits between your internet connection and every device in your house. It forces ALL traffic through a VPN before any device ever touches the internet. If the VPN drops, the internet stops. No exceptions, no leaks, no millisecond gaps.

> "The absolute easiest way to track your online behaviors is through your home IP address. A cheap VPN application is not sufficient. We need stable protection and a backup plan if a VPN connection should fail."
>
> — Michael Bazzell, *Extreme Privacy*

## What this protects

| Device | Without Firewall | With pfSense + VPN |
|---|---|---|
| **Your laptop** | Leaks real IP to Apple/Microsoft on every boot before VPN app connects | VPN is always on at the network level — device never sees your real IP |
| **Your phone on Wi-Fi** | Apple/Google constantly receive your home IP through background services | All Wi-Fi traffic routed through VPN — Apple/Google see a shared VPN IP |
| **Smart TV / Roku / Fire Stick** | Streaming services know your exact home IP, link it to your payment | Streaming services see VPN IP shared by thousands of people |
| **Smart home devices** | Ring, Nest, Alexa all phone home with your real IP and location | Devices can't expose your real IP even if they try |
| **Guest devices** | Anyone connecting to your Wi-Fi exposes your home IP through their accounts | Guest traffic goes through VPN — your home IP stays hidden |
| **When VPN drops** | VPN app silently disconnects, traffic flows unprotected until you notice | Kill switch: internet stops entirely until VPN reconnects. Zero leakage. |

## The hardware

The firewall is a small, silent, fanless computer that runs 24/7 between your modem and your router. Bazzell recommends the **Protectli Vault** — a compact device purpose-built for running pfSense. It draws very little power, has no moving parts, and fits in the palm of your hand. He's had one running non-stop for over five years.

**🔒 Protectli Vault FW2B — ~$300**
: 2 ethernet ports. Suitable for simple setups — one device directly connected. Good for single users with no Wi-Fi needs.

**⭐ Protectli Vault FW4B — ~$400**
: 4 ethernet ports. **Bazzell's recommendation for most clients.** Handles VPN speeds up to 200–250 Mbps. Supports the "Netflix port" workaround. Enough for most homes.

**🚀 Protectli Vault FW6B — ~$600**
: 6 ethernet ports. For gigabit internet, large households, or heavy streaming. Faster VPN throughput. Choose this if you have very high-speed internet and multiple demanding users.

### Additional hardware you'll need

| Item | Purpose | Cost |
|---|---|---|
| **GL.iNet Beryl or Slate** | Portable Wi-Fi router. Connects to pfSense's LAN port and broadcasts Wi-Fi for all your wireless devices. No proprietary software — runs on OpenWRT. | ~$60–$80 |
| **Ethernet cables (2–3)** | Connect modem → pfSense, pfSense → Wi-Fi router, pfSense → your laptop (wired is always preferred). | ~$10 |
| **USB flash drive (4GB+)** | Used to install pfSense onto the Protectli Vault. Only needed once during initial setup. | ~$5 |
| **USB keyboard + monitor** | Needed temporarily during pfSense installation only. Disconnect after setup — the firewall runs headless. | Borrow for 30 min |
| **UPS battery backup** | Protects firewall, modem, and router from power outages. Prevents corruption and keeps internet alive during brief outages. Bazzell considers this essential. | ~$50–$70 |

:::tip[Total hardware cost]
For the recommended setup (FW4B + Beryl + UPS + cables): approximately **$530–$560 one-time**. No monthly hardware fees. The Protectli Vault lasts years. The only ongoing cost is your VPN subscription (~$5–10/month for ProtonVPN).
:::

:::caution[CPU requirement]
Whatever hardware you choose, ensure the CPU supports **AES-NI** (Advanced Encryption Standard New Instructions). This hardware-accelerated encryption is critical for VPN performance and may be required by future pfSense versions. All Protectli Vault models support it.
:::

## Network architecture

Bazzell presents several configurations depending on your household needs. Here are the most relevant ones for a household with multiple people who need both privacy and streaming.

### Option A: The recommended household setup

```
Cable Modem → pfSense Firewall (VPN + Kill Switch)
                      ├→ Wi-Fi Router #1 "Home" → All devices (VPN protected)
                      └→ Wi-Fi Router #2 "Streaming" (no VPN) → Netflix, Hulu, etc.
```

This is Bazzell's recommended setup for households where some members need streaming services that block VPNs. Personal devices connect to the "Home" network (fully VPN-protected). Streaming devices connect to the "Streaming" network (direct connection, no VPN). You pick your battles — privacy protected where it matters, while other household members can still watch Netflix.

### Option B: Maximum privacy (single network)

```
Cable Modem → pfSense Firewall (VPN + Kill Switch) → Wi-Fi Router → All devices
```

If you live alone or everyone in your house accepts that some streaming services won't work, this is simplest. Everything goes through the VPN, period. Some streaming services may be blocked — ProtonVPN actually works with many of them, but Netflix is hit-or-miss.

### Option C: Wired-only (Bazzell's personal setup)

```
Cable Modem → pfSense Firewall (VPN + Kill Switch) → Laptop via Ethernet
```

Bazzell works this way most of the time — laptop connected directly to the firewall via ethernet cable. No Wi-Fi broadcasting at all. He only turns on Wi-Fi when his mobile device needs it. The less wireless signal you broadcast, the less can be intercepted or detected from outside your home.

## pfSense installation: step-by-step

Bazzell provides a detailed multi-phase tutorial. Here's the full process condensed into actionable steps with the reasoning behind each one. **Practice this once without connecting to the internet**, then wipe and start fresh when you're confident.

### Phase 1: Install pfSense onto the Protectli Vault

**1. Create the installation USB.** Go to **pfsense.org/download**. Choose Architecture: AMD64, Installer: USB Memstick, Console: VGA. Download the .gz file and decompress it to get the .img file. Download **Etcher** (balena.io/etcher). Use Etcher to flash the .img file onto a USB drive.

**2. Install pfSense on the Vault.** Connect a monitor and USB keyboard to the Vault. Insert the USB drive. Power on. If it doesn't boot from USB, press F11 repeatedly on startup to access the boot menu. Accept all default installation options. When prompted for ZFS Configuration, select your drive and press spacebar to select it. Choose "No" if asked to open a shell. Choose "Reboot" when complete.

**3. Initial configuration.** After reboot, power down. Remove USB, monitor, and keyboard. Connect an ethernet cable from your **computer to the LAN port** and from your **modem to the WAN port**. Make sure your computer has no other internet connection (disable Wi-Fi). Navigate to `192.168.1.1` in your browser. Log in with username `admin`, password `pfsense`. Accept defaults, create a strong password when prompted. Click through until you reach the dashboard.

### Phase 2: Activate extra ports (4-port and 6-port models)

**4. Add and bridge ports.** Navigate to `Interfaces → Assignments`. Click "Add" next to each empty port until all are added. Click through each new interface (Opt1, Opt2, etc.), enable each one, and save. Then go to `Interfaces → Assignments → Bridges`, create a new bridge selecting LAN + all Opt ports. Add a firewall rule for the bridge (`Firewall → Rules → Bridge`) with Protocol set to "Any". This lets all physical ports act as one network.

### Phase 3: Configure the VPN (ProtonVPN)

**5. Download ProtonVPN certificate.** Log into your ProtonVPN account. Navigate to `account.protonvpn.com/downloads`. Under OpenVPN Configuration Files, select **Router → UDP → Standard Server Configs**. Choose a server in your country and download the certificate file. Open it in a text editor — you'll need to copy sections from it.

**6. Add the certificate to pfSense.** In pfSense: `System → Cert Manager → CAs → Add`. Set the name to "VPN". Change Method to "Import an existing Certificate Authority". Copy the certificate text from the downloaded file (the block between BEGIN CERTIFICATE and END CERTIFICATE) into the certificate field. Save.

**7. Configure the OpenVPN client.** Navigate to `VPN → OpenVPN → Clients → Add`. Configure with the settings from the ProtonVPN certificate file — server address, port, protocol (UDP), encryption algorithm, and your ProtonVPN username/password. This is the most technical step — Bazzell provides exact field-by-field instructions in the book, and ProtonVPN has a pfSense setup guide on their support site. The key settings: TLS authentication, AES-256-CBC cipher, SHA-512 auth digest.

### Phase 4: Configure DNS (Cloudflare encrypted)

**8. Set up encrypted DNS.** Navigate to `System → General Setup`. Add `1.1.1.1` as DNS server with hostname `cloudflare-dns.com`, interface WAN_DHCP. Add `1.0.0.1` as second DNS server with same settings. Disable "DNS server override". Change DNS Resolution Behavior to "Use remote DNS server, ignore local DNS". Save.

Then go to `Services → DNS Resolver → General Settings`. Enable DNS Resolver. Under Outgoing Network Interfaces, select "OVPNC". Enable "DNS Query Forwarding" and "Use SSL/TLS for outgoing DNS Queries". In Custom Options, add the forwarding configuration for Cloudflare's DNS over TLS (port 853). Save, apply, reboot.

:::note[Why Cloudflare on the firewall, not NextDNS?]
Bazzell recommends Cloudflare on the firewall because it's unfiltered — it won't accidentally block websites or services across your entire network. He uses **NextDNS with filtering on individual devices** (configured in the browser or OS level) so each person can customize their own ad-blocking without affecting the whole household. The firewall DNS is the fallback that handles any device that doesn't have its own DNS configured.
:::

### Phase 5: Enable the kill switch

**9. Lock all traffic to the VPN.** This is the most important security configuration. Navigate to `Firewall → Rules → LAN`. Edit the "Default allow LAN to any rule". Click "Display Advanced" and change the Gateway to `OVPNC_VPNV4` (your VPN interface). Save and apply. Then disable the IPv6 rule. Go to `System → Advanced → Miscellaneous` and enable both "State Killing on Gateway Failure" and "Skip rules when gateway is down". Save and reboot.

Now **if the VPN ever drops, the internet stops completely**. No traffic can leave your network without going through the VPN tunnel. This is the kill switch.

**10. Test the kill switch.** Go to `Status → OpenVPN` and click the stop button to manually kill the VPN. Try to load any website. It should fail completely — no connection. This confirms the kill switch works. Reboot the firewall to restore the VPN connection.

Then verify your protection at these sites:

```
https://dnsleaktest.com       — Run Extended Test. Only your DNS provider should appear.
https://browserleaks.com/ip   — Should show your VPN IP, not your real IP.
https://www.deviceinfo.me     — Should show VPN details, not your ISP.
```

### Phase 6: Enable AES-NI and PowerD

**11. Hardware acceleration and power management.** Go to `System → Advanced → Miscellaneous`. Under Cryptographic & Thermal Hardware, select "AES-NI CPU-based Acceleration". Under Power Savings, enable "PowerD" with "Hiadaptive" for each option. Save. This may improve VPN throughput and reduces power consumption during idle periods.

## Adding Wi-Fi: connecting the GL.iNet router

pfSense has no built-in Wi-Fi (the optional internal card is slow and limited range). Instead, you connect a separate Wi-Fi router to pfSense's LAN port. The router acts purely as a Wi-Fi access point — pfSense handles all the security.

**1. Connect the router to pfSense.** Power on the GL.iNet Beryl/Slate. Connect an ethernet cable from the router's **WAN port** to pfSense's **LAN port**. Connect to the router's Wi-Fi from your phone or laptop.

**2. Configure as access point mode.** Navigate to `192.168.8.1` in your browser. Set a strong admin password. Go to `Wireless → 2.4G WiFi → Modify`. Rename the SSID to something private (not your name or address). Set a strong Wi-Fi password. Repeat for 5G WiFi. Then go to `More Settings → Network Mode → Access Point → Apply`.

**3. Verify VPN protection on Wi-Fi.** Connect any device to the new Wi-Fi network. Visit `dnsleaktest.com` and `browserleaks.com/ip`. You should see your VPN IP address, not your real one. Every device on this Wi-Fi network is now protected by pfSense's VPN.

:::tip[Range note]
The GL.iNet routers are portable/travel-sized, so range is shorter than a full-size home router. Bazzell notes he's installed them in three-story homes without major issues. A potential benefit: the limited range means your Wi-Fi signal doesn't broadcast far outside your home, making it harder for neighbors or passersby to detect.
:::

## The "Netflix Port" — for households that need streaming

Many streaming services (Netflix, Hulu, Disney+) block VPN IP addresses. If you need these services, you can configure the **last port on your Protectli Vault** to bypass the VPN and connect directly to your ISP. Anything plugged into this port — or a second Wi-Fi router connected to it — has **no VPN protection** but can access all streaming services.

:::caution[Privacy tradeoff]
Devices on the Netflix port expose your real home IP to your ISP and the streaming service. Use this ONLY for streaming. Never connect your personal laptop, phone, or any device with accounts tied to your identity to this port. Keep a strict separation: personal devices on the VPN-protected network, entertainment devices on the streaming network.
:::

The configuration involves creating a separate DHCP range (192.168.2.x) on the last port, setting its firewall gateway to WAN_DHCP (direct internet, no VPN), and disabling gateway monitoring on that interface. Bazzell provides the exact steps — your pfSense dashboard walks you through each setting. The result: two completely separate networks from one box.

Connect a second GL.iNet router to this port in access point mode and name its Wi-Fi something like "Streaming". Household members connect entertainment devices to "Streaming" for Netflix, and everything else to your main VPN-protected network.

## ISP & modem setup

### Get a modem without Wi-Fi

If your ISP gave you a combined modem/router/Wi-Fi device, this creates problems. Its built-in Wi-Fi bypasses pfSense entirely, and its router function can conflict with pfSense's IP addressing. The ideal solution: request a **modem-only device** from your ISP (no router, no Wi-Fi). If that's not available, disable Wi-Fi and DHCP on the ISP device completely, and never plug anything directly into it. Everything goes through pfSense.

### IP conflict resolution

If your ISP router uses the 192.168.1.x IP range (most do), it will conflict with pfSense's default range. Either change the ISP router to a different range (like 192.168.9.x) or change pfSense's range. Bazzell's preference: change the ISP router so pfSense stays at its default.

### Your internet service itself

Internet service should be in the name of your **trust or LLC**, not your personal name. Your ISP already knows your home's physical location (they installed the cable), but having the account in a trust name prevents your personal name from appearing in their subscriber lists that get sold to marketing companies.

## Ongoing maintenance

### Daily

Bazzell shuts his firewall down every night and powers it back on in the morning. This forces a fresh VPN connection daily and prevents stale connections. A quick press of the power button shuts pfSense down properly (takes ~20 seconds). **Never hold the power button or pull the cord** — this can corrupt the operating system.

### Occasionally

Test for DNS leaks at `dnsleaktest.com`. Verify your VPN IP at `browserleaks.com/ip`. Check for pfSense updates on the Dashboard page. Minor updates (2.6.1, 2.6.2) are usually safe. Major updates (2.7.0) — **always backup your configuration first**.

### Backup your configuration

Navigate to `Diagnostics → Backup & Restore`. Click "Download configuration as XML". Save the file with a descriptive name like `4-Port-ProtonVPN-US.xml`. Store it in your encrypted VeraCrypt container. If your firewall ever gets corrupted, you can reinstall pfSense and import this file to restore every setting instantly.

:::note[Pre-made configuration files]
Bazzell hosts pre-made pfSense configuration files at **inteltechniques.com/firewall** that include all the settings from his book. These can dramatically speed up setup if you're comfortable importing a config file rather than configuring every setting manually. However, he recommends doing it manually at least once so you understand what each setting does.
:::

### When your internet "goes out"

If you suddenly lose internet, it's almost always the VPN disconnecting (which triggers the kill switch — working as designed). Open your browser and go to `192.168.1.1` (you can always reach pfSense locally even without internet). Navigate to `Status → OpenVPN`. Click the restart button. Internet should return within seconds. If not, reboot the firewall with the power button.

## Taking your protection on the road (travel router)

The GL.iNet Beryl/Slate is also a travel router. When you're at a hotel, it sits between you and the hostile hotel Wi-Fi — protecting your devices with a VPN even away from home.

**1. Connect a secondary device to hotel Wi-Fi first.** Use a non-personal device (a cheap burner phone) to connect to the hotel Wi-Fi and authorize through their login portal. This registers that device's MAC address with the hotel's network.

**2. Clone the MAC address to your travel router.** Disconnect the burner from hotel Wi-Fi. Connect to your travel router instead. Open `192.168.8.1`, navigate to `More Settings → MAC Clone`. Select the burner's MAC address under "Client" and apply it to "Your Router". The hotel network now thinks your router IS the authorized device.

**3. Connect your real devices to the travel router.** All your personal devices connect to the travel router's Wi-Fi, which tunnels everything through the VPN. The hotel sees one device (your router). Your devices never touch the hotel network directly. Your traffic is encrypted end-to-end.

## Total investment

**🔧 One-time hardware — ~$540–$610**
: Protectli Vault FW4B ($400) + GL.iNet Beryl ($70) + UPS ($60) + cables ($10). Optional: second Beryl for streaming network ($70) or travel.

**📡 Monthly VPN — included / ~$5–10/mo**
: ProtonVPN Plus plan. Already included in your Proton Family subscription from the [master roadmap](/privacy/). If not, standalone pricing applies.

**⏱️ Setup time — one afternoon**
: First-time setup: 2–4 hours including practice run. Subsequent rebuilds (from backup config): 30 minutes.

## The complete home network security checklist

### Hardware shopping

- [ ] Purchase Protectli Vault FW4B (or FW6B for gigabit internet)
- [ ] Purchase GL.iNet Beryl router (primary Wi-Fi)
- [ ] Purchase second GL.iNet Beryl (for streaming network or travel) — optional
- [ ] Purchase APC UPS battery backup
- [ ] Have ethernet cables, USB keyboard, and monitor available for setup

### pfSense installation

- [ ] Download pfSense .img and flash to USB drive with Etcher
- [ ] Install pfSense on Protectli Vault (monitor + keyboard required temporarily)
- [ ] Complete initial setup wizard — create strong admin password
- [ ] Activate and bridge extra ports (4-port and 6-port models)

### VPN configuration

- [ ] Download ProtonVPN OpenVPN certificate (Router → UDP → Standard)
- [ ] Import certificate into pfSense Cert Manager
- [ ] Configure OpenVPN client with ProtonVPN credentials
- [ ] Configure encrypted DNS (Cloudflare 1.1.1.1 over TLS)
- [ ] Enable kill switch (LAN gateway → VPN, state killing, skip rules on gateway down)
- [ ] Enable AES-NI hardware acceleration and PowerD

### Wi-Fi & streaming

- [ ] Connect GL.iNet Beryl to pfSense LAN port — configure as access point
- [ ] Rename Wi-Fi SSID and set strong password
- [ ] Configure Netflix port on last Protectli port (optional — for streaming)
- [ ] Connect second Beryl to Netflix port for streaming Wi-Fi (optional)
- [ ] Disable Wi-Fi on ISP modem/router if applicable

### Testing & verification

- [ ] Test kill switch: stop VPN manually, confirm internet stops
- [ ] Verify VPN IP at browserleaks.com/ip — should NOT show your real IP
- [ ] Run extended DNS leak test at dnsleaktest.com — only Cloudflare should appear
- [ ] Test from Wi-Fi device — confirm VPN protection carries to wireless
- [ ] Backup pfSense configuration as XML — store in encrypted container
- [ ] Plug firewall, modem, and router into UPS battery backup

---

**Home Network Security Guide**

Based on *Extreme Privacy: What It Takes to Disappear* by Michael Bazzell, Chapter 4: Home Network. Pre-made configuration files available at inteltechniques.com/firewall. This guide is for educational purposes — always verify current pfSense documentation before configuring.
