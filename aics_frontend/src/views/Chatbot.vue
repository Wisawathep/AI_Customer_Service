<template>
  <div class="app">
    <main class="main">
        <ChatBox />
    </main>
  </div>
</template>

<script setup>
import ChatBox from "@/components/ChatBox.vue";
</script>

<style scoped>

.app{
    min-height:100vh;

    background:
    linear-gradient(
        135deg,
        #F8F5F0,
        #EEE7DB
    );

    display:flex;
    flex-direction:column;
}

/* ================= Header ================= */

.header{

    height:80px;

    display:flex;
    align-items:center;
    gap:18px;

    padding:0 40px;

    background:#FCFAF7;

    border-bottom:1px solid #DDD3C5;

    box-shadow:0 2px 12px rgba(0,0,0,.05);

}

.logo{

    width:54px;
    height:54px;

    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:26px;

    background:#6B7A52;
    color:white;

}

.header h1{

    margin:0;

    color:#5E503F;

    font-size:28px;

}

.header p{

    margin-top:4px;

    color:#8C7B68;

    font-size:14px;

}

/* ================= Main ================= */

.main{

    flex:1;

    display:flex;

    justify-content:center;

    align-items:center;

    padding:0px;

}

/* ================= Chat ================= */

.chat-card{

    width:1200px;

    height:90vh;

    background:#FCFAF7;

    border-radius:22px;

    overflow:hidden;

    border:1px solid #E3DACF;

    box-shadow:
    0 15px 45px rgba(0,0,0,.12);

}

</style>