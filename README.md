# BrainstormingAgent

Workspace khusus untuk **Brainstorming Agent** berbasis Antigravity Customizations (`AGENTS.md` + `.agents/skills/`). Dirancang untuk membantu eksplorasi ide project, tugas, ide bisnis, maupun pengambilan keputusan secara terstruktur.

## Struktur Project

```text
BrainstormingAgent/
├── AGENTS.md                           # Aturan utama, persona, & workflow git
├── README.md                           # Dokumentasi workspace
├── .agents/
│   └── skills/
│       ├── ideation-facilitator/       # Eksplorasi ide (SCAMPER, First Principles, HMW)
│       ├── business-validator/         # Validasi bisnis (Lean Canvas, ICP, monetisasi)
│       ├── project-scoper/             # Pemecahan ide jadi MVP & task breakdown
│       ├── devils-advocate/            # Uji ketahanan ide, risiko, & blind spot
│       └── idea-logger/                # Arsip hasil diskusi ke folder ideas/
└── ideas/                              # Hasil brainstorming tersimpan (.md)
```

## Cara Pakai

1. Buka folder ini sebagai workspace di Antigravity.
2. Mulai obrolan dengan topik apa pun, misalnya:
   - *"Aku mau brainstorm ide SaaS buat UMKM..."*
   - *"Bantu validasi ide bisnis ini..."*
   - *"Pecah ide project ini jadi MVP dan daftar tugas."*
   - *"Kritisi rencanaku ini, cari kelemahannya."*
   - *"Simpan hasil diskusi kita barusan."*
3. Agent akan otomatis memuat skill yang relevan dan (jika diminta/disetujui) menyimpan ringkasan ke `ideas/` serta commit + push ke GitHub.
