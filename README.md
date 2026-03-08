# AI Dịch Thuật Anh - Việt
Dự án ứng dụng trí tuệ nhân tạo để dịch thuật từ tiếng Anh sang tiếng Việt, được tối ưu hóa cho máy tính có cấu hình thấp bằng kỹ thuật **LoRA (Low-Rank Adaptation)**.

## Giới thiệu
Mô hình này được Fine-tune từ mô hình gốc `Helsinki-NLP/opus-mt-en-vi` sử dụng tập dữ liệu chuẩn. Thay vì huấn luyện lại toàn bộ hàng chục triệu tham số, dự án áp dụng kỹ thuật LoRA để chỉ huấn luyện một lớp adapter cực nhỏ (chỉ chiếm ~1-2% tổng tham số). Điều này giúp giảm thiểu tối đa yêu cầu về phần cứng (VRAM) mà vẫn giữ được chất lượng dịch thuật rất tốt.

## Tính năng
* **Siêu nhẹ:** Adapter LoRA chỉ nặng vài MB, dễ dàng lưu trữ và chia sẻ.
* **Tốc độ nhanh:** Chạy mượt mà trên cả CPU nhờ sử dụng kiến trúc gọn nhẹ.
* **Giao diện thân thiện:** Được xây dựng bằng Streamlit, cho phép người dùng nhập văn bản và xem kết quả dịch ngay lập tức trên trình duyệt.

## Công nghệ
* **Ngôn ngữ:** Python 3.x
* **AI/Deep Learning Framework:** PyTorch, Transformers (Hugging Face)
* **Tối ưu hóa tài nguyên:** PEFT (LoRA), BitsAndBytes
* **Giao diện Web:** Streamlit

## Hướng dẫn chạy trên máy tính

**Bước 1: Clone dự án và di chuyển vào thư mục**
```bash
git clone <link-repo-cua-ban>
cd <ten-thu-muc-repo>
```

**Bước 2: Cài đặt các thư viện cần thiết**
```bash
pip install -r requirements.txt
```

**Bước 3: Khởi chạy ứng dụng Web**
```bash
streamlit run app.py
```
Mở trình duyệt và truy cập vào `http://localhost:8501` để sử dụng.
