# About Sen (senbuzy.com) — 100% Clone

Bản clone 100% đầy đủ từ website [about.senbuzy.com](https://about.senbuzy.com/) (portfolio của Sen Zheng - Creative Technologist).

## 🚀 Tính năng & Thành phần đã clone đầy đủ (100%)

- **3D Interactive Model**: Mô hình 3D `man2.glb` (Three.js r169) phản hồi chuột/chuyển động kèm môi trường ánh sáng HDR `env.hdr` và shader noise overlay.
- **Toàn bộ video tác phẩm**: 43 video định dạng MP4/M4V/MOV chất lượng cao trong thư mục `works/`.
- **Toàn bộ hình ảnh & ảnh bìa**: Toàn bộ WebP, JPG, PNG trong các thư mục `works/` và `images/`.
- **Đa ngôn ngữ**: Chuyển đổi mượt mà giữa tiếng Anh (EN) và tiếng Trung (ZH).
- **Trình chiếu tương tác**: Các modal chi tiết từng dự án (Guqin, Campus Time Machine, Dog Code Clothes, Glass Wall Arcade, ZOOOP, SoBricks, Raymarching...).

## 📁 Cấu trúc thư mục

```text
.
├── index.html                 # Trang HTML chính
├── assets/                    # Bundle JS & CSS
│   ├── index-CYaUks6u.css
│   └── index-Xi6D-mUj.js
├── models/                    # Mô hình 3D
│   └── man2.glb
├── textures/                  # Texture HDR cho ánh sáng 3D
│   └── env.hdr
├── images/                    # Ảnh đại diện, logo
│   ├── bp.png
│   ├── buzyzheng.png
│   └── hotsar.jpg
├── works/                     # Toàn bộ video và hình ảnh các dự án
│   ├── anim/
│   ├── blender/
│   ├── covers/
│   ├── dog-code-clothes/
│   ├── glass-wall-arcade/
│   ├── guqin/
│   ├── other-ads/
│   ├── other-side-works/
│   ├── raymarching/
│   ├── retro-game-wedding/
│   ├── sobricks/
│   ├── switch-cat-house/
│   ├── time-machine/
│   ├── webgl/
│   └── zooop/
├── server.py                  # Server Python tối ưu MIME & video streaming
├── package.json
└── README.md
```

## 🛠️ Cách chạy trang web

### Cách 1: Sử dụng Python (khuyên dùng, không cần cài đặt thêm gì)
```bash
python3 server.py
# hoặc:
python3 server.py 8080
```
Mở trình duyệt tại [http://localhost:3000](http://localhost:3000) (hoặc cổng bạn chọn).

### Cách 2: Sử dụng Node.js / npm
```bash
npm start
# hoặc:
npx serve . -p 3000
```
