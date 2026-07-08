<template>
  <div
    class="message"
    :class="message.role"
  >

    <template v-if="message.role === 'assistant' && message.thinking">
      <div class="loading-bubble">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </template>

    <template v-else>
      {{ message.content }}
    </template>

  </div>
</template>

<script setup>
defineProps({
  message: Object,
});
</script>

<style scoped>
.message {
  max-width: 70%;
  padding: 12px;
  margin: 10px;
  border-radius: 10px;
  word-wrap: break-word;
}

.user {
  background: #007bff;
  color: white;
  margin-left: auto;
}

.assistant {
  background: #e5e5e5;
}

.loading-bubble{
    display:flex;
    gap:6px;
}

.loading-bubble span{
    width:8px;
    height:8px;
    border-radius:50%;
    background:#777;
    animation:bounce 1.2s infinite;
}

.loading-bubble span:nth-child(2){
    animation-delay:.2s;
}

.loading-bubble span:nth-child(3){
    animation-delay:.4s;
}

@keyframes bounce{

    0%,80%,100%{
        transform:scale(.5);
        opacity:.3;
    }

    40%{
        transform:scale(1);
        opacity:1;
    }

}
</style>