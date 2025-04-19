# 🤖 MLArchitectBot

MLArchitectBot is a smart AI-powered chatbot built for Discord using the `discord.py` library. It responds to user messages using a large language model backend and includes utility commands like message clearing for moderators.

---

## 🚀 Features

- 🧠 **Conversational AI**: Responds to user messages using `llmbotmodel` which leverages llama.
- 🧹 **Message Management**: `!clear` command to bulk delete messages in a channel.
- ⚡ **Fast & Asynchronous**: Uses `asyncio` for efficient operation.

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Niall1985/MLArchitectBot.git
cd MLArchitectBot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Dependencies:
> - `discord.py`
> - `python-dotenv`

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```
key=YOUR_DISCORD_BOT_TOKEN
```

### 4. Enable Privileged Intents

Go to the [Discord Developer Portal](https://discord.com/developers/applications), select your bot, then go to **Bot > Privileged Gateway Intents**, and enable:
- `MESSAGE CONTENT INTENT`

---

## 📜 Commands

### `!clear [amount]`

Deletes the specified number of messages in the current channel. Defaults to `100`.

> ⚠️ Requires `Manage Messages` permission.

---

## 📂 File Structure

```
.
├── bot.py            
├── llmbotmodel.py
├── llm_helper.py     
├── .env
├── .gitignore               
├── LICENSE
└── README.md           
```

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

Made with 💻 by **[Niall1985](https://github.com/Niall1985)**  
Feel free to fork, star ⭐, or contribute!

---

Let me know if you want the actual `LICENSE` file generated too!