<template>
  <div class="home">

    <!-- ================= HERO ================= -->

    <section class="hero">

      <div class="hero-blob" aria-hidden="true"></div>

      <div class="hero-left">

        <span class="eyebrow">🐾 ร้านอาหารและอุปกรณ์สัตว์เลี้ยง</span>

        <h1>Pet Shop</h1>
        <h2>AI Customer Service</h2>

        <p>
          ยินดีต้อนรับสู่ร้านจำหน่ายอาหารและอุปกรณ์สัตว์เลี้ยงออนไลน์
          พร้อมผู้ช่วย AI ที่สามารถตอบคำถามเกี่ยวกับสินค้า
          การจัดส่ง การชำระเงิน และบริการต่าง ๆ ได้ตลอด 24 ชั่วโมง
        </p>

        <router-link to="/chatbot">
          <button class="chat-btn">
            💬 เริ่มพูดคุยกับ AI
          </button>
        </router-link>

      </div>

      <div class="hero-right">

        <div class="pet-card">
          <span class="pet-card-ring"></span>
          <div class="pet-card-emojis">
            <span>🐕</span><span>🐈</span><span>🐇</span><span>🦜</span>
          </div>
          <span class="pet-card-label">Happy&nbsp;Pets</span>
        </div>

      </div>

    </section>

    <!-- divider -->
    <div class="paw-divider" aria-hidden="true">
      <span>🐾</span><span>🐾</span><span>🐾</span><span>🐾</span><span>🐾</span>
    </div>

    <!-- ================= FEATURES ================= -->

    <section class="features">

      <span class="section-eyebrow">ทำไมต้องเลือกเรา</span>
      <h2>บริการที่ใส่ใจทุกรายละเอียด</h2>

      <div class="feature-grid">

        <div class="feature">
          <span class="feature-icon">🐾</span>
          <h3>สินค้าของแท้</h3>
          <p>
            จำหน่ายสินค้าจากผู้ผลิตและตัวแทนจำหน่ายที่ได้รับการรับรอง
          </p>
        </div>

        <div class="feature">
          <span class="feature-icon">🚚</span>
          <h3>จัดส่งรวดเร็ว</h3>
          <p>
            จัดส่งสินค้าทั่วประเทศไทย พร้อมติดตามสถานะการจัดส่ง
          </p>
        </div>

        <div class="feature">
          <span class="feature-icon">💬</span>
          <h3>AI Customer Service</h3>
          <p>
            ตอบคำถามเกี่ยวกับสินค้า การชำระเงิน และบริการได้ตลอด 24 ชั่วโมง
          </p>
        </div>

        <div class="feature">
          <span class="feature-icon">❤️</span>
          <h3>ใส่ใจสัตว์เลี้ยง</h3>
          <p>
            คัดเลือกสินค้าที่มีคุณภาพ เพื่อสุขภาพและความปลอดภัยของสัตว์เลี้ยง
          </p>
        </div>

      </div>

    </section>

    <!-- ================= PRODUCTS ================= -->

    <section class="products">

      <span class="section-eyebrow">เลือกช้อปได้เลย</span>
      <h2>หมวดหมู่สินค้ายอดนิยม</h2>

      <div class="product-grid">

        <div class="product-card">
          <span class="product-emoji">🦴</span>
          <h3>อาหารสุนัข</h3>
        </div>

        <div class="product-card">
          <span class="product-emoji">🐱</span>
          <h3>อาหารแมว</h3>
        </div>

        <div class="product-card">
          <span class="product-emoji">🎾</span>
          <h3>ของเล่นสัตว์เลี้ยง</h3>
        </div>

        <div class="product-card">
          <span class="product-emoji">🛁</span>
          <h3>อุปกรณ์ดูแลสัตว์เลี้ยง</h3>
        </div>

      </div>

    </section>

    <!-- ================= FOOTER ================= -->

    <footer>

      <div class="footer-wave" aria-hidden="true"></div>

      <h3>🐾 Pet Shop AI Customer Service</h3>

      <p>
        ผู้ช่วยอัจฉริยะสำหรับตอบคำถามเกี่ยวกับสินค้า การสั่งซื้อ
        การชำระเงิน และบริการของร้าน
      </p>

    </footer>

  </div>
</template>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Mali:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Quicksand:wght@300..700&display=swap');

*{
  box-sizing:border-box;
}

.home{

  --color-bg:#F5EFE2;
  --color-bg-alt:#EAE0CB;
  --color-moss:#4B5A2F;
  --color-moss-dark:#3A4624;
  --color-clay:#B5652E;
  --color-clay-dark:#98531F;
  --color-text:#3B3025;
  --color-text-soft:#6E6152;
  --color-card:#FFFCF5;

  --font-heading:'Mali', sans-serif;
  --font-body:'Mali', sans-serif;

  background:var(--color-bg);
  color:var(--color-text);
  font-family:var(--font-body);
  overflow-x:hidden;

}

h1,h2,h3{
  font-family:var(--font-heading);
  font-weight:400;
}

/* HERO */

.hero{

  position:relative;

  min-height:85vh;

  display:flex;
  justify-content:space-between;
  align-items:center;

  padding:100px 10% 80px;

}

.hero-blob{

  position:absolute;
  top:-120px;
  right:-160px;

  width:520px;
  height:520px;

  background:radial-gradient(circle at 30% 30%, #C9AE7C 0%, var(--color-bg-alt) 70%);

  border-radius:42% 58% 65% 35% / 45% 40% 60% 55%;

  opacity:.6;

  z-index:0;

}

.hero-left{

  position:relative;
  z-index:1;

  width:55%;

}

.eyebrow{

  display:inline-block;

  background:rgba(75,90,47,.1);

  color:var(--color-moss-dark);

  padding:8px 18px;

  border-radius:30px;

  font-size:14px;

  font-weight:600;

  letter-spacing:.5px;

  margin-bottom:22px;

}

.hero-left h1{

  font-size:64px;
  line-height:1.1;
  color:var(--color-moss-dark);

}

.hero-left h2{

  margin-top:6px;

  color:var(--color-clay);

  font-size:30px;

}

.hero-left p{

  margin:30px 0 36px;

  font-size:18px;

  line-height:1.85;

  color:var(--color-text-soft);

  max-width:520px;

}

.chat-btn{

  background:var(--color-moss);

  color:#FFFCF5;

  border:none;

  padding:18px 42px;

  font-family:var(--font-body);

  font-weight:600;

  font-size:17px;

  border-radius:50px;

  cursor:pointer;

  box-shadow:0 12px 24px rgba(75,90,47,.28);

  transition:transform .25s ease, background .25s ease, box-shadow .25s ease;

}

.chat-btn:hover{

  background:var(--color-moss-dark);

  transform:translateY(-3px);

  box-shadow:0 16px 30px rgba(75,90,47,.35);

}

.hero-right{

  position:relative;
  z-index:1;

  width:35%;

  display:flex;

  justify-content:center;

}

.pet-card{

  position:relative;

  width:300px;

  height:300px;

  border-radius:50%;

  background:var(--color-card);

  display:flex;

  flex-direction:column;

  justify-content:center;

  align-items:center;

  gap:14px;

  box-shadow:0 20px 45px rgba(75,58,36,.18);

}

.pet-card-ring{

  position:absolute;

  inset:-14px;

  border:2px dashed var(--color-clay);

  border-radius:50%;

  opacity:.5;

  animation:spin 40s linear infinite;

}

@keyframes spin{
  from{ transform:rotate(0deg); }
  to{ transform:rotate(360deg); }
}

.pet-card-emojis{

  font-size:46px;

  display:flex;

  gap:10px;

}

.pet-card-label{

  font-family:'Chonburi', sans-serif;

  font-size:16px;

  color:var(--color-moss-dark);

  letter-spacing:.5px;

}

/* PAW DIVIDER */

.paw-divider{

  display:flex;

  justify-content:center;

  gap:60px;

  font-size:22px;

  opacity:.35;

  padding:10px 0 30px;

  transform:rotate(-8deg);

}

.paw-divider span:nth-child(even){

  transform:translateY(10px);

}

/* SECTION HEADINGS */

.section-eyebrow{

  display:block;

  color:var(--color-clay);

  font-weight:600;

  font-size:15px;

  letter-spacing:1px;

  margin-bottom:10px;

}

/* FEATURES */

.features{

  padding:60px 10% 90px;

  text-align:center;

}

.features h2{

  margin-bottom:55px;

  font-size:32px;

  color:var(--color-moss-dark);

}

.feature-grid{

  display:grid;

  grid-template-columns:repeat(auto-fit,minmax(250px,1fr));

  gap:28px;

}

.feature{

  background:var(--color-card);

  border-radius:22px;

  padding:38px 30px;

  text-align:left;

  box-shadow:0 12px 28px rgba(75,58,36,.08);

  border-bottom:4px solid transparent;

  transition:transform .25s ease, border-color .25s ease, box-shadow .25s ease;

}

.feature:hover{

  transform:translateY(-6px);

  border-bottom-color:var(--color-clay);

  box-shadow:0 18px 34px rgba(75,58,36,.14);

}

.feature-icon{

  display:inline-flex;

  align-items:center;

  justify-content:center;

  width:60px;

  height:60px;

  border-radius:18px;

  background:rgba(181,101,46,.12);

  font-size:30px;

}

.feature h3{

  margin:22px 0 12px;

  font-size:20px;

  color:var(--color-moss-dark);

}

.feature p{

  color:var(--color-text-soft);

  line-height:1.7;

  font-size:15px;

}

/* PRODUCTS */

.products{

  background:var(--color-bg-alt);

  padding:90px 10%;

  text-align:center;

}

.products h2{

  margin-bottom:55px;

  font-size:32px;

  color:var(--color-moss-dark);

}

.product-grid{

  display:grid;

  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

  gap:26px;

}

.product-card{

  background:var(--color-card);

  border-radius:22px;

  padding:44px 20px;

  box-shadow:0 12px 24px rgba(75,58,36,.1);

  transition:transform .25s ease, box-shadow .25s ease;

}

.product-card:nth-child(even){

  transform:rotate(1.2deg);

}

.product-card:nth-child(odd){

  transform:rotate(-1.2deg);

}

.product-card:hover{

  transform:translateY(-6px) rotate(0deg);

  box-shadow:0 18px 32px rgba(75,58,36,.16);

}

.product-emoji{

  font-size:52px;

  display:block;

}

.product-card h3{

  margin-top:18px;

  font-size:19px;

  color:var(--color-moss-dark);

  font-family:var(--font-heading);

  font-weight:600;

}

/* FOOTER */

footer{

  position:relative;

  background:var(--color-moss-dark);

  color:#F5EFE2;

  text-align:center;

  padding:70px 20px 46px;

  overflow:hidden;

}

.footer-wave{

  position:absolute;

  top:-1px;

  left:0;

  width:100%;

  height:40px;

  background:var(--color-bg-alt);

  border-radius:0 0 50% 50% / 0 0 100% 100%;

}

footer h3{

  font-size:22px;

}

footer p{

  margin-top:16px;

  opacity:.85;

  max-width:520px;

  margin-left:auto;

  margin-right:auto;

  line-height:1.7;

  font-size:15px;

}

/* RESPONSIVE */

@media (max-width:900px){

  .hero{

    flex-direction:column-reverse;

    text-align:center;

    padding:70px 6% 60px;

  }

  .hero-left, .hero-right{

    width:100%;

  }

  .hero-left p{

    margin-left:auto;

    margin-right:auto;

  }

  .hero-left h1{

    font-size:46px;

  }

  .hero-blob{

    display:none;

  }

  .paw-divider{

    gap:30px;

  }

}

@media (prefers-reduced-motion: reduce){

  .pet-card-ring{

    animation:none;

  }

}

</style>