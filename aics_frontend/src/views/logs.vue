<template>
  <div class="container">

    <div class="page-header">
      <div class="header-left">
        <h1>🧠 Logging Dashboard</h1>
        <span class="entry-count">{{ logsHistory.length }} รายการ</span>
      </div>

      <div class="header-actions">
        <button class="btn-live" :class="{ active: isLive }" @click="toggleLive">
          <span class="live-dot" v-if="isLive"></span>
          {{ isLive ? "Live" : "Live: Off" }}
        </button>

        <button @click="loadLogs">
          ⟳ Refresh
        </button>
      </div>
    </div>

    <div v-if="logsHistory.length === 0" class="empty-state">
      ยังไม่มีข้อมูล log
    </div>

    <div class="terminal">

      <div class="terminal-topbar">
        <span class="tb-dot red"></span>
        <span class="tb-dot yellow"></span>
        <span class="tb-dot green"></span>
        <span class="tb-title">pipeline.log</span>
      </div>

      <div class="terminal-body">

        <div
          v-for="(entry, i) in logsHistory"
          :key="entry.id"
          class="log-line-group"
        >

          <!-- ===== สรุป 1 บรรทัด (คลิกเพื่อขยาย) ===== -->
          <div class="log-summary" @click="toggleExpand(entry.id)">

            <span class="caret">{{ expandedIds.has(entry.id) ? '▾' : '▸' }}</span>

            <span class="log-time">{{ formatTime(entry.timestamp) }}</span>

            <span class="log-badge" v-if="i === 0">NEW</span>

            <span
              class="tag"
              :class="entry.data.input_guardrail.status === 'PASS' ? 'tag-pass' : 'tag-fail'"
            >
              IN:{{ entry.data.input_guardrail.status }}
            </span>

            <span
              class="tag"
              :class="entry.data.retrieval_guardrail.status === 'PASS' ? 'tag-pass' : 'tag-fail'"
            >
              RET:{{ entry.data.retrieval_guardrail.status }}
            </span>

            <span class="tag tag-info">
              {{ entry.data.retriever.retrieved }} chunks
            </span>

            <span class="log-question">
              {{ entry.data.question }}
            </span>

          </div>

          <!-- ===== รายละเอียดเต็ม (ขยายเมื่อคลิก) ===== -->
          <div class="log-detail" v-if="expandedIds.has(entry.id)">

            <div class="detail-row">
              <span class="prompt">$</span>
              <span class="key">question</span>
              <span class="val">{{ entry.data.question }}</span>
            </div>

            <div class="detail-row">
              <span class="prompt">$</span>
              <span class="key">input_guardrail</span>
              <span
                class="tag"
                :class="entry.data.input_guardrail.status === 'PASS' ? 'tag-pass' : 'tag-fail'"
              >
                {{ entry.data.input_guardrail.status }}
              </span>
              <span class="val-dim">{{ entry.data.input_guardrail.reason }}</span>
            </div>

            <div class="detail-row">
              <span class="prompt">$</span>
              <span class="key">retriever</span>
              <span class="val">retrieved {{ entry.data.retriever.retrieved }} chunks</span>
            </div>

            <div
              class="chunk-block"
              v-for="(chunk, index) in entry.data.retriever.chunks"
              :key="index"
            >
              <div class="chunk-head">
                <span class="chunk-tag">chunk[{{ index }}]</span>
                <span class="chunk-meta">distance: {{ chunk.distance }}</span>
              </div>
              <pre class="chunk-preview">{{ chunk.preview }}</pre>
            </div>

            <div class="detail-row">
              <span class="prompt">$</span>
              <span class="key">retrieval_guardrail</span>
              <span
                class="tag"
                :class="entry.data.retrieval_guardrail.status === 'PASS' ? 'tag-pass' : 'tag-fail'"
              >
                {{ entry.data.retrieval_guardrail.status }}
              </span>
              <span class="val-dim">
                before: {{ entry.data.retrieval_guardrail.before }} → after: {{ entry.data.retrieval_guardrail.after }}
              </span>
            </div>

            <div class="detail-row" v-if="entry.data.retrieval_guardrail.reason">
              <span class="indent"></span>
              <span class="val-dim">{{ entry.data.retrieval_guardrail.reason }}</span>
            </div>

            <div class="detail-row">
              <span class="prompt">$</span>
              <span class="key">prompt_builder</span>
              <span class="val">context_length: {{ entry.data.prompt_builder.context_length }}</span>
            </div>

            <div class="detail-row">
              <span class="prompt">$</span>
              <span class="key">output_guardrail</span>
              <span class="val">supported: {{ entry.data.output_guardrail.supported }}</span>
            </div>

            <div class="detail-row" v-if="entry.data.output_guardrail.reason">
              <span class="indent"></span>
              <span class="val-dim">{{ entry.data.output_guardrail.reason }}</span>
            </div>

            <div class="detail-row answer-row">
              <span class="prompt">$</span>
              <span class="key">answer</span>
            </div>
            <pre class="answer-block">{{ entry.data.answer }}</pre>

          </div>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>

import axios from "axios"

import { ref, onMounted, onUnmounted } from "vue"

const logsHistory = ref([])
const isLive = ref(false)
let pollInterval = null

async function loadLogs(){

    const res = await axios.get(

        "http://localhost:8000/logs"

    )

    addLogEntry(res.data)

}

function addLogEntry(data){

  const serialized = JSON.stringify(data)

  const last = logsHistory.value[0]
  if (last && last.serialized === serialized) return

  logsHistory.value.unshift({
    id: Date.now() + Math.random(),
    timestamp: new Date(),
    data,
    serialized
  })

}

function toggleLive(){

  isLive.value = !isLive.value

  if (isLive.value) {
    pollInterval = setInterval(loadLogs, 3000)
  } else {
    clearInterval(pollInterval)
  }

}

function formatTime(date){
  return date.toLocaleTimeString("th-TH", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit"
  })
}

/* ===== เพิ่มใหม่: คุมการขยาย/ย่อของแต่ละ log entry (UI เท่านั้น) ===== */
const expandedIds = ref(new Set())

function toggleExpand(id){
  const next = new Set(expandedIds.value)
  if (next.has(id)) {
    next.delete(id)
  } else {
    next.add(id)
  }
  expandedIds.value = next
}

onMounted(loadLogs)

onUnmounted(() => clearInterval(pollInterval))

</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Mali:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

* {
  box-sizing: border-box;
}

.container{

    max-width:1100px;

    margin:auto;

    padding:50px 24px 80px;

    font-family:'Mali', sans-serif;

    background:#F8F5F0;

    min-height:100vh;

    color:#4E4338;

}

/* ================= PAGE HEADER ================= */
.page-header{
  display:flex;
  align-items:center;
  justify-content:space-between;
  flex-wrap:wrap;
  gap:16px;
  margin-bottom:28px;
}

.header-left{
  display:flex;
  align-items:baseline;
  gap:12px;
  flex-wrap:wrap;
}

h1{
  margin:0;
  font-size:28px;
  color:#5E503F;
  font-weight:700;
}

.entry-count{
  font-size:13px;
  color:#8A7A63;
  background:#EEE7DB;
  padding:4px 14px;
  border-radius:20px;
  font-weight:600;
}

.header-actions{
  display:flex;
  gap:10px;
}

button{

    background:#6B7A52;

    color:white;

    border:none;

    padding:12px 26px;

    border-radius:30px;

    cursor:pointer;

    font-family:'Mali', sans-serif;

    font-size:15px;

    font-weight:600;

    transition:.25s;

    box-shadow:0 8px 20px rgba(107,122,82,.25);

}

button:hover{

    background:#556340;

    transform:translateY(-2px);

}

.btn-live{
  background:#FFFFFF;
  color:#6B7A52;
  border:1px solid #D9CFC0;
  box-shadow:none;
  display:flex;
  align-items:center;
  gap:8px;
}

.btn-live:hover{
  background:#F8F5F0;
  color:#556340;
  transform:none;
}

.btn-live.active{
  background:#DCE9D5;
  color:#2F5A3A;
  border-color:#B7D4A8;
}

.live-dot{
  width:8px;
  height:8px;
  border-radius:50%;
  background:#3F8A4C;
  display:inline-block;
  animation:pulse 1.4s infinite;
}

@keyframes pulse{
  0%,100%{ box-shadow:0 0 0 0 rgba(63,138,76,.4); }
  50%{ box-shadow:0 0 0 5px rgba(63,138,76,0); }
}

/* ================= EMPTY STATE ================= */
.empty-state{
  text-align:center;
  padding:60px 20px;
  color:#A79B8A;
  font-size:15px;
  background:#FFFFFF;
  border:1px dashed #D9CFC0;
  border-radius:20px;
}

/* ================= TERMINAL WINDOW ================= */
.terminal{
  background:#2B241C;
  border-radius:16px;
  overflow:hidden;
  box-shadow:0 20px 45px rgba(43,36,28,.35);
  border:1px solid #4A3F30;
}

.terminal-topbar{
  display:flex;
  align-items:center;
  gap:8px;
  padding:12px 16px;
  background:#38301F;
  border-bottom:1px solid #4A3F30;
}

.tb-dot{
  width:11px;
  height:11px;
  border-radius:50%;
  display:inline-block;
}

.tb-dot.red{ background:#E0665B; }
.tb-dot.yellow{ background:#E0B85B; }
.tb-dot.green{ background:#7FB86A; }

.tb-title{
  margin-left:10px;
  font-family:'JetBrains Mono', monospace;
  font-size:12.5px;
  color:#B8AC97;
}

.terminal-body{
  padding:10px 8px;
  font-family:'JetBrains Mono', monospace;
  font-size:13px;
  max-height:none;
}

/* ================= LOG SUMMARY LINE ================= */
.log-line-group{
  border-bottom:1px solid #3A3225;
}

.log-line-group:last-child{
  border-bottom:none;
}

.log-summary{
  display:flex;
  align-items:center;
  gap:10px;
  padding:10px 12px;
  cursor:pointer;
  flex-wrap:wrap;
  transition:.15s;
  border-radius:6px;
}

.log-summary:hover{
  background:#3A3225;
}

.caret{
  color:#7FB86A;
  width:12px;
  flex-shrink:0;
}

.log-time{
  color:#8A7C63;
  font-size:12px;
  flex-shrink:0;
}

.log-badge{
  background:#7FB86A;
  color:#1F2A17;
  font-size:10.5px;
  font-weight:700;
  padding:2px 8px;
  border-radius:10px;
  flex-shrink:0;
}

.log-question{
  color:#E8DFC8;
  font-size:13px;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  flex:1;
  min-width:120px;
}

/* ================= TAGS ================= */
.tag{
  font-size:11px;
  font-weight:600;
  padding:2px 9px;
  border-radius:10px;
  white-space:nowrap;
  flex-shrink:0;
}

.tag-pass{
  background:rgba(127,184,106,.15);
  color:#8FCB78;
}

.tag-fail{
  background:rgba(224,102,91,.15);
  color:#E88C82;
}

.tag-info{
  background:rgba(184,172,151,.12);
  color:#B8AC97;
}

/* ================= DETAIL EXPANDED ================= */
.log-detail{
  padding:4px 12px 18px 34px;
  display:flex;
  flex-direction:column;
  gap:6px;
  animation:fadeIn .15s ease;
}

@keyframes fadeIn{
  from{ opacity:0; transform:translateY(-4px); }
  to{ opacity:1; transform:translateY(0); }
}

.detail-row{
  display:flex;
  align-items:center;
  gap:8px;
  flex-wrap:wrap;
  font-size:12.5px;
}

.prompt{
  color:#7FB86A;
  font-weight:700;
}

.indent{
  width:14px;
  flex-shrink:0;
}

.key{
  color:#E0B85B;
  font-weight:600;
}

.val{
  color:#D8CEB8;
}

.val-dim{
  color:#8A7C63;
  font-style:italic;
}

.answer-row{
  margin-top:6px;
}

/* ================= CHUNK BLOCK ================= */
.chunk-block{
  background:#221C15;
  border-left:2px solid #4A3F30;
  border-radius:6px;
  padding:8px 12px;
  margin:2px 0 2px 14px;
}

.chunk-head{
  display:flex;
  gap:12px;
  flex-wrap:wrap;
  font-size:11.5px;
  margin-bottom:4px;
}

.chunk-tag{
  color:#E0B85B;
  font-weight:600;
}

.chunk-meta{
  color:#8A7C63;
}

.chunk-preview,
.answer-block{
  white-space:pre-wrap;
  color:#C9BFA8;
  font-size:12px;
  line-height:1.55;
  margin:0;
  padding:8px 10px;
  background:#221C15;
  border-radius:6px;
  border:1px solid #3A3225;
}

.answer-block{
  margin-left:14px;
  color:#E8DFC8;
}

/* ================= RESPONSIVE ================= */
@media (max-width:640px){

  .container{
    padding:30px 16px 60px;
  }

  .page-header{
    flex-direction:column;
    align-items:flex-start;
  }

  h1{
    font-size:22px;
  }

  .log-summary{
    font-size:12px;
  }

  .log-question{
    min-width:100%;
    order:99;
    white-space:normal;
  }

}

</style>