# 🔍 Advanced Subdomain Finder Tool

A powerful and beginner-friendly Python tool to find subdomains of any domain using `crt.sh` and optional `subfinder`, check their live status, categorize them, and save results to a `.txt` file.

## ✨ Features

- ✅ Uses **crt.sh** and **subfinder** for subdomain enumeration
- 🌐 Checks if subdomains are live
- 🧠 Auto-categorizes subdomains (Admin Panel, API, Blog, etc.)
- 💾 Saves output in a clean `.txt` file
- ⚙️ No API keys needed
- 🐧 Linux & Windows compatible

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### 2. Run the Script

```bash
Advance Subdomain.py
```

You will be asked:
```
Enter domain (e.g., example.com):
```

It will fetch subdomains, check live status, and save the result in:

```
example_com_subdomains.txt
```

---

## ⚙️ Optional Dependencies

To enhance results using [subfinder](https://github.com/projectdiscovery/subfinder):

```bash
sudo apt install subfinder
```

---

## 📂 Output Format

```
Subdomain                     Status    Category
------------------------------------------------------
admin.example.com             200       Admin Panel
api.example.com               200       API Endpoint
shop.example.com              301       E-Commerce
```

---

## 📜 License

MIT License

---

## 🙋‍♂️ Author

Made with ❤️ by [Shadab Khan](https://github.com/yourusername)
