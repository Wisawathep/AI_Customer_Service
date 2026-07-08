<template>
  <div class="chat-page">

    <!-- ================= HEADER ================= -->
    <div class="chat-header">
      <div class="header-pattern"></div>

      <div class="chat-avatar">🐾</div>
      <div class="chat-header-text">
        <h2>Pet Shop AI</h2>
        <span class="status">
          <i class="dot"></i> ออนไลน์ตลอด 24 ชม.
        </span>
      </div>

      <div class="header-badge">✨ ผู้ช่วยอัจฉริยะ</div>
    </div>

    <!-- ================= MESSAGES ================= -->
    <div class="messages">
      <div class="messages-inner">

        <div class="date-divider">
          <span>วันนี้</span>
        </div>

        <MessageItem
          v-for="(msg, index) in messages"
          :key="index"
          :message="msg"
        />

      </div>
    </div>

    <!-- ================= INPUT ================= -->
    <div class="input-wrapper">
      <div class="input-inner">

        <div class="quick-chips" v-if="messages.length <= 1">
          <button
            v-for="q in quickQuestions"
            :key="q"
            class="chip"
            @click="askQuick(q)"
            :disabled="loading"
          >
            {{ q }}
          </button>
        </div>

        <div class="input-area">
          <input
            v-model="userMessage"
            @keyup.enter="sendMessage"
            placeholder="พิมพ์ข้อความ..."
          />

          <button
            @click="sendMessage"
            :disabled="loading"
          >
            {{ loading ? "กำลังส่ง..." : "ส่ง" }}
          </button>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from "vue";
import { API_BASE_URL } from "../services/config";
import MessageItem from "./MessageItem.vue";

const userMessage = ref("");
const loading = ref(false);
let sessionId = localStorage.getItem("session_id");

if (!sessionId) {
  sessionId = crypto.randomUUID();
  localStorage.setItem("session_id", sessionId);
}

const messages = ref([
  {
    role: "assistant",
    content: "สวัสดีครับ มีอะไรให้ช่วยไหม",
  },
]);

const sendMessage = async () => {
  if (!userMessage.value.trim()) return;

  const messageText = userMessage.value;

  messages.value.push({
    role: "user",
    content: messageText,
  });

  userMessage.value = "";
  loading.value = true;

    messages.value.push({
      role: "assistant",
      content: "",
      thinking: true
    });

    const assistantIndex = messages.value.length - 1;

    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          session_id: sessionId,
          message: messageText,
        }),
    });
    
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    if (!response.body) {
      throw new Error("ReadableStream not yet supported in this browser.");
    }
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let firstChunk = true;

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      if (firstChunk) {
        messages.value[assistantIndex].thinking = false;
        firstChunk = false;
      }

      const chunk = decoder.decode(value, { stream: true });
            for (const char of chunk) {
              messages.value[assistantIndex].content += char;
              await new Promise(resolve =>
                setTimeout(resolve, 15)
              );
            }}

  } catch (error) {
    messages.value[assistantIndex].thinking = false;
    messages.value[assistantIndex].content = "เกิดข้อผิดพลาด";

    console.error(error);
  } finally {
    loading.value = false;
  }
};

/* ===== เพิ่มใหม่: ปุ่มคำถามแนะนำเหนือช่องพิมพ์ (แสดงเฉพาะตอนยังไม่เริ่มคุย) ===== */
const quickQuestions = [
  "ค่าจัดส่งเท่าไหร่?",
  "มีอาหารแมวยี่ห้อไหนบ้าง?",
  "ชำระเงินได้ช่องทางไหนบ้าง?",
];

const askQuick = (question) => {
  userMessage.value = question;
  sendMessage();
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Mali:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Quicksand:wght@300..700&display=swap');
* {
  box-sizing: border-box;
}

/* ================= PAGE ================= */
.chat-page {
  width: 100%;
  height: 100vh;
  margin: 0;
  display: flex;
  flex-direction: column;
  font-family: 'Mali', sans-serif;
  background:
    radial-gradient(circle at 15% 10%, rgba(107,122,82,0.06), transparent 40%),
    radial-gradient(circle at 85% 90%, rgba(94,80,63,0.06), transparent 40%),
    #F8F5F0;
  overflow: hidden;

  --font-heading:'Mali', sans-serif;
  --font-body:'Mali', sans-serif;
}

/* ================= HEADER ================= */
.chat-header {
  position: relative;
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 24px 32px;
  background: linear-gradient(135deg, #6B7A52, #4E5B36);
  color: #fff;
  overflow: hidden;
  flex-shrink: 0;
}

.header-pattern {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255,255,255,0.08) 2px, transparent 2px);
  background-size: 22px 22px;
  opacity: .6;
  pointer-events: none;
}

.chat-avatar {
  position: relative;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.18);
  border: 2px solid rgba(255,255,255,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  flex-shrink: 0;
}

.chat-header-text {
  position: relative;
  z-index: 1;
}

.chat-header-text h2 {
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: .01em;
}

.status {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  opacity: 0.9;
  margin-top: 4px;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #A6D96A;
  display: inline-block;
  box-shadow: 0 0 0 3px rgba(166, 217, 106, 0.3);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 3px rgba(166, 217, 106, 0.3); }
  50% { box-shadow: 0 0 0 6px rgba(166, 217, 106, 0.15); }
}

.header-badge {
  position: relative;
  margin-left: auto;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.25);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  white-space: nowrap;
  backdrop-filter: blur(4px);
}

@media (max-width: 640px) {
  .header-badge { display: none; }
}

/* ================= MESSAGES ================= */
.messages {
  flex: 1;
  overflow-y: auto;
  padding: 28px 20px;
}

.messages-inner {
  max-width: 780px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.messages::-webkit-scrollbar {
  width: 8px;
}

.messages::-webkit-scrollbar-thumb {
  background: #D9CFC0;
  border-radius: 10px;
}

.messages::-webkit-scrollbar-track {
  background: transparent;
}

.date-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.date-divider span {
  background: #EEE7DB;
  color: #8A7A63;
  font-size: 12px;
  font-weight: 600;
  padding: 6px 16px;
  border-radius: 20px;
}

/* LOADING BUBBLE (ใช้ใน MessageItem) */
.loading-bubble {
  width: fit-content;
  background: #EEE7DB;
  border-radius: 18px;
  padding: 12px 16px;
  display: flex;
  gap: 5px;
}

.loading-bubble span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #8A7A63;
  display: inline-block;
  animation: bounce 1.2s infinite;
}

.loading-bubble span:nth-child(2) { animation-delay: .2s; }
.loading-bubble span:nth-child(3) { animation-delay: .4s; }

@keyframes bounce {
  0%, 80%, 100% { transform: scale(0.6); opacity: .3; }
  40% { transform: scale(1); opacity: 1; }
}

/* ================= INPUT ================= */
.input-wrapper {
  flex-shrink: 0;
  background: linear-gradient(180deg, rgba(248,245,240,0), #F8F5F0 30%);
  padding: 12px 20px 24px;
}

.input-inner {
  max-width: 780px;
  margin: 0 auto;
}

.quick-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 12px;
}

.chip {
  background: #FFFFFF;
  border: 1px solid #E2D9C9;
  color: #6B7A52;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: .2s;
  white-space: nowrap;
}

.chip:hover:not(:disabled) {
  background: #6B7A52;
  color: #fff;
  border-color: #6B7A52;
  transform: translateY(-2px);
}

.chip:disabled {
  opacity: .5;
  cursor: not-allowed;
}

.input-area {
  display: flex;
  gap: 12px;
  background: #FFFFFF;
  padding: 8px 8px 8px 20px;
  border-radius: 30px;
  border: 1px solid #EEE7DB;
  box-shadow: 0 10px 30px rgba(94, 80, 63, 0.1);
  font-family: var(--font-body);
}

input {
  flex: 1;
  padding: 12px 0;
  border: none;
  background: transparent;
  font-size: 15px;
  font-family: var(--font-body);
  color: #4E4338;
  outline: none;
}

input::placeholder {
  color: #A79B8A;
}

button {
  min-width: 100px;
  background: #6B7A52;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 24px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
  transition: .25s;
}

button:hover:not(:disabled) {
  background: #556340;
  transform: translateY(-2px);
}

button:disabled {
  background: #C9BFAE;
  cursor: not-allowed;
  transform: none;
}

/* ================= RESPONSIVE ================= */
@media (max-width: 640px) {
  .chat-header { padding: 18px 20px; }
  .messages { padding: 20px 14px; }
  .input-wrapper { padding: 8px 14px 18px; }
}
</style>