# AI Agent Framework Comparison

Repositori ini berisi eksplorasi *hands-on* terhadap tiga framework AI Agent *open-source* populer: **Agno (Phidata)**, **LlamaIndex**, dan **CrewAI**. 

Tujuan dari proyek ini adalah untuk menganalisis kelebihan dan kekurangan masing-masing *tool* berdasarkan eksperimen langsung, serta menentukan framework terbaik untuk kasus penggunaan (*use case*) tertentu.

## Skenario Uji
Evaluasi dilakukan menggunakan satu skenario uji yang identik untuk ketiga framework:
*   **Tugas:** Agent bertindak sebagai Analis Data Produk. Agent menerima data *revenue* dan *cost*, memanggil *custom tool* `calculate_profit` untuk menghitung laba bersih, lalu menyusun laporan ringkas.
*   **LLM:** OpenAI (`gpt-4o-mini`)
*   **Prompt Dasar:** "Kamu adalah analis data produk. Gunakan tool yang tersedia untuk menghitung profit dari data yang diberikan, lalu berikan laporan ringkas."

## Tabel Komparasi Framework

Tabel di bawah ini merupakan ringkasan dari hasil eksekusi dan analisis arsitektur masing-masing framework:

| Kriteria / Variabel | Agno (Phidata) | LlamaIndex | CrewAI |
| :--- | :--- | :--- | :--- |
| **Kemudahan Setup & Konfigurasi** | Sangat intuitif dan *Pythonic*. Kode instansiasi paling ringkas tanpa butuh banyak *boilerplate*. | Moderat. Membutuhkan pemahaman abstraksi framework (seperti *Agent Runner* dan *Query Engine*). | *Setup* berjenjang wajib (*Agent*, *Task*, *Crew*). Sangat terstruktur namun *overkill* untuk *single-task*. |
| **Kecepatan Eksekusi (Latency)** | **Tercepat (7.02 detik).** Sangat efisien dengan beban pemrosesan minimal untuk aplikasi *real-time*. | **Paling Lambat (51.36 detik).** Kinerja moderat dengan fokus pada peringkasan bahasa tanpa manipulasi data lanjutan. | **Cepat (30.52 detik).** Menyeimbangkan kedalaman logika (membuat tabel markdown dan kalkulasi persentase) dengan latensi optimal. |
| **Manajemen State / Memory** | Sangat modern dengan integrasi memori persisten bawaan (Postgres/SQLite) yang mudah disiapkan. | Berbasis dokumen; menggunakan `ChatMemoryBuffer` dan sangat terintegrasi dengan *Vector Database*. | Otomatis terpusat pada `Crew`. Konteks (*state*) diwariskan antar agen secara implisit tanpa kode tambahan. |
| **Kemampuan Multi-Agent / Tooling** | *Tooling Pythonic* (fungsi standar). Mendukung pendelegasian agen dasar, namun kurang cocok untuk alur kolaborasi kompleks. | Sangat kaya *Data Tools* via LlamaHub. Multi-agent tersedia, namun lebih optimal untuk orkestrasi pencarian data (RAG). | Arsitektur terbaik untuk multi-agent. Mendukung kolaborasi sekuensial dan hierarkis secara *out-of-the-box*. |
| **Kelebihan Utama** | Waktu respons sangat rendah. Sangat berfokus pada integrasi cepat dengan abstraksi kode yang bersih. | Keseimbangan yang baik antara struktur dokumen dan waktu tunggu. Kompatibilitas tanpa batas dengan sumber data. | Otomatisasi analisis setara analis manusia; format pelaporan sangat profesional, terstruktur mandiri, dan siap dipresentasikan. |
| **Kekurangan Utama** | Kurang inisiatif dalam memformat data kompleks secara visual; output bersifat statis. | Tidak menyajikan data komparatif yang lebih mendalam dibanding Agno meskipun latensinya lebih lama. | Membutuhkan penulisan kode yang panjang untuk konfigurasi awal, menjadikannya kurang praktis untuk tugas sederhana. |
| **Rekomendasi Case Penggunaan** | Integrasi *backend* API yang menuntut *response time* tinggi, pembuatan *microservices* ringan, atau *chatbot* fungsional cepat. | Sistem *Retrieval-Augmented Generation* (RAG) tingkat lanjut dan *chatbot* perusahaan yang terhubung dengan ribuan dokumen internal. | Pembuatan laporan otomatis komprehensif, orkestrasi alur kerja *multi-agent* kompleks, dan tugas *batch-processing* asinkron. |

## Kesimpulan
Dari hasil pengujian, terlihat spesialisasi yang jelas dari tiap framework:
1.  Gunakan **Agno** jika Anda membangun aplikasi interaktif yang sangat mengutamakan kecepatan *(low-latency)* dan efisiensi kode.
2.  Gunakan **CrewAI** jika Anda membutuhkan agen yang mampu berpikir mendalam, melakukan penalaran lanjutan, dan menyajikan data kompleks dalam format profesional (sistem pelaporan asinkron).
3.  Gunakan **LlamaIndex** jika aplikasi Anda sangat bergantung pada pencarian data dari ratusan dokumen internal atau *database* *(RAG-heavy operations)*.