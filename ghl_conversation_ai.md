# GoHighLevel (GHL) — Conversation AI: Complete Documentation

## What Is Conversation AI?

Conversation AI is GoHighLevel's built-in AI chatbot and messaging automation system. It uses large language model technology to handle inbound conversations across multiple channels — qualifying leads, answering questions, and booking appointments — without manual intervention.

It operates inside the GHL **Conversations** inbox and can work in three modes: fully automated, suggestive (human-assisted), or off.

---

## Bot Modes

| Mode | Behavior |
|------|----------|
| **Off** | Bot is inactive. No AI responses. |
| **Suggestive** | AI drafts a reply for the human agent to review and send. |
| **Auto-Pilot** | Bot responds automatically to every inbound message. |

---

## Supported Channels

Conversation AI can be deployed across all major messaging channels:

- **SMS**
- **Facebook Messenger**
- **Instagram DM**
- **Live Chat / Web Chat Widget**
- **WhatsApp**
- **Email** (limited)
- **Voice AI** (via the Voice AI Chat Widget — separate feature)

Channels are configured in **Settings → Conversation AI → Supported Channels**.

---

## Setup Methods

### 1. Guided Form-Based Setup
A structured wizard that walks you through the bot configuration step by step. You define the bot's goal, and GHL builds the conversation logic behind the scenes. Best for beginners.

### 2. Flow-Based Builder (Conversation AI V3)
A visual drag-and-drop canvas for building complex conversation flows. You can:
- Add conditions, triggers, and actions
- Branch the conversation based on user responses
- Assign to multiple calendars
- Integrate with workflows

**Steps to create a bot:**
1. Go to **Settings → Conversation AI**
2. Click **"Create Bot"**
3. Choose a template: *General Q&A* or *Appointment Booking*
4. Edit the prompt and configure channels
5. Train the bot with your knowledge sources
6. Set the bot to **Suggestive** or **Auto-Pilot**

---

## Bot Templates

| Template | Use Case |
|----------|----------|
| **General Q&A** | Customer support, answering FAQs, product/service inquiries |
| **Appointment Booking** | Lead qualification + scheduling calls or classes |

---

## Training the Bot (Knowledge Base)

The bot is trained using two complementary systems:

### Web Crawler
- Crawls your website and extracts content (features, testimonials, pricing, contact info, service descriptions)
- Supports up to **4,000 URLs** per knowledge base
- Mimics real visitor behavior: opens accordions, clicks tabs, scrolls to reveal dynamic content
- **Success rate: ~94.7%** across site types (up from 81.6%)
- Modes: Exact-URL, Domain, and Path crawling

### Custom Bot Responses (FAQs)
- Manually define precise question-and-answer pairs
- Ensures consistent, accurate answers for critical topics
- Takes priority over web-crawled content when a match is found

### File Uploads
- Supported formats: **PDF, DOCX, PPT, TXT, spreadsheets**
- Content is auto-chunked and indexed for semantic search
- Ideal for pricing sheets, onboarding guides, product manuals

---

## Appointment Booking via Conversation AI

The bot can qualify a lead and book an appointment in a single conversation:

1. Bot asks qualifying questions (customizable)
2. Bot checks calendar availability in real time
3. Bot confirms and books the slot
4. Confirmation emails/SMS and reminders fire automatically via workflows

**Multi-calendar support:** The AI intelligently selects the right calendar based on the scenario (e.g. trial class vs. consultation call).

**Setup path:** Settings → Conversation AI → Create Bot → Template: *Appointment Booking* → link to calendar.

---

## Advanced Settings

| Setting | Description |
|---------|-------------|
| **Wait time before responding** | Delay (in seconds) before the bot replies; 5–20s recommended for a natural feel |
| **Max message limit** | Cap on how many messages the bot sends in a single thread |
| **Send Bot to Sleep** | Temporarily pauses the bot when a human takes over; prevents interruptions |
| **Bot handoff** | Route conversation to a human agent when the bot cannot resolve the query |
| **Stop bot on reply** | Halts auto-pilot when a team member replies manually |

---

## Multi-Modal Capabilities

Conversation AI supports more than plain text:

| Input Type | What the Bot Can Do |
|------------|---------------------|
| **Images** | Read screenshots, identify uploaded documents, recognize visual content |
| **Audio messages** | Transcribe and understand voice messages; extract names, dates, amounts, intent |
| **Text** | Full natural-language understanding and response |

---

## Workflow Integration

Conversation AI works natively with GHL **Workflows**:

- **Trigger:** "Conversation AI message received" or "Contact replied"
- **Action — Conversation AI Bot:** Send a bot response inside a workflow step
- **Action — Send Bot to Sleep:** Pause the bot for a defined duration
- **Action — Wake Bot:** Resume the bot after a manual interaction
- Use workflow branches to route leads based on bot-collected data (e.g. qualification score, intent)

---

## API & Webhook Integration

GHL exposes the Conversation AI system via its REST API and webhook system:

- **Inbound Webhook trigger:** receive events from external platforms (TikTok, Shopify, etc.) and feed them into a Conversation AI workflow
- **Conversations API:** programmatically send/receive messages, update contact records
- **API docs:** available at the HighLevel Marketplace developer portal
- Supports real-time webhook events for: message received, appointment booked, contact updated, conversation status changed

---

## All-In-One Chat Widget

GHL's chat widget bundles multiple channels into a single embeddable UI:

- Live Chat
- SMS / Email opt-in
- WhatsApp
- Facebook Messenger
- Instagram
- **Voice AI** (speak directly with an AI receptionist)

The Conversation AI bot powers the automated layer behind this widget.

---

## Key 2025–2026 Updates

| Update | Detail |
|--------|--------|
| **V3 Flow Builder** | Full drag-and-drop canvas replacing the legacy prompt editor |
| **Enhanced Web Crawler** | 5.2× more content captured; 94.7% success rate |
| **Image understanding** | Bot reads and responds to images shared in chat |
| **Audio understanding** | Bot transcribes and responds to voice messages |
| **Multi-calendar booking** | AI picks the right calendar automatically |
| **Expanded file uploads** | PDF, DOCX, PPT, spreadsheets as knowledge sources |
| **Improved prompt logic** | More natural, on-topic, context-aware responses |

---

## Official Documentation Links

- [Setting Up Conversation AI](https://help.gohighlevel.com/support/solutions/articles/155000004401-setting-up-conversation-ai)
- [Conversation AI Bot Explained](https://help.gohighlevel.com/support/solutions/articles/155000001335-conversation-ai-bot-explained)
- [Flow Builder Setup Guide](https://help.gohighlevel.com/support/solutions/articles/155000006515-conversation-ai-flow-builder)
- [Guided Form-Based Setup](https://help.gohighlevel.com/support/solutions/articles/155000005382-guided-form-based-setup-for-conversation-ai)
- [Advanced Bot Settings](https://help.gohighlevel.com/support/solutions/articles/155000004415-advanced-settings-overview-conversation-ai)
- [Training Your Bot (Web Crawler & FAQs)](https://help.gohighlevel.com/support/solutions/articles/155000004416-training-your-conversation-ai-bot)
- [New Knowledge Sources & Quality Upgrades](https://help.gohighlevel.com/support/solutions/articles/155000006456-conversation-ai-new-knowledge-sources-quality-upgrades)
- [Enhanced Web Crawler](https://help.gohighlevel.com/support/solutions/articles/155000006625-knowledge-base-enhanced-web-crawler)
- [Appointment Booking via Conversation AI](https://help.gohighlevel.com/support/solutions/articles/155000000210-how-to-use-conversation-ai-to-book-appointments)
- [AI Conversational Appointment Booking Workflow](https://help.gohighlevel.com/support/solutions/articles/48001216782-ai-conversational-appointment-booking-workflow-and-setup)
- [Workflow Actions — Conversation AI](https://help.gohighlevel.com/support/solutions/articles/155000001358-workflow-actions-conversation-ai)
- [Voice AI Chat Widget Setup](https://help.gohighlevel.com/support/solutions/articles/155000006648-how-to-set-up-and-use-the-voice-ai-chat-widget)
- [Conversation AI & Voice AI — API Docs](https://marketplace.gohighlevel.com/docs/marketplace-modules/ConversationsAIandVoiceAI/index.html)
- [All AI Tools in HighLevel](https://help.gohighlevel.com/support/solutions/articles/155000002166-ai-tools-in-highlevel)
