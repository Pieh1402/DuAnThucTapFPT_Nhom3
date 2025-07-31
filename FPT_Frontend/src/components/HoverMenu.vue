<template>
  <v-menu open-on-hover>
    <template v-slot:activator="{ props }">
      <v-btn text class="menu-btn text-black" v-bind="props">
        <span class="menu-title">{{ title }}</span>
        <v-icon v-if="icon" end>{{ icon }}</v-icon>
      </v-btn>
    </template>

    <slot />
  </v-menu>
</template>

<script setup lang="ts">
defineProps<{ title: string; icon?: string }>();
</script>

<style scoped>
.menu-btn {
  position: relative;
  transition: all 0.3s ease;
}

/* Phần chữ */
.menu-title {
  position: relative;
  display: inline-block;
  font-weight: 500;
  transition: font-weight 0.3s ease;
}

/* Gạch dọc mặc định mờ */
.menu-title::before,
.menu-title::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  width: 1px;
  background-color: rgba(0, 0, 0, 0); /* Gạch nhạt lúc đầu */
  transition: background-color 0.3s ease;
}

.menu-title::before {
  left: -8px;
}

.menu-title::after {
  right: -8px;
}

/* Khi hover */
.menu-btn:hover .menu-title {
  animation: shakeX 0.3s ease;
  animation-fill-mode: forwards; /* giữ lại trạng thái cuối */
}

.menu-btn:hover .menu-title::before,
.menu-btn:hover .menu-title::after {
  background-color: rgba(0, 0, 0, 0.9); /* Gạch đậm hơn */
}

/* Shake ngang */
@keyframes shakeX {
  0% {
    transform: translateX(0);
    font-weight: 500;
  }
  25% {
    transform: translateX(-2px);
  }
  50% {
    transform: translateX(2px);
  }
  75% {
    transform: translateX(-1px);
  }
  100% {
    transform: translateX(0);
    font-weight: 700;
  }
}
</style>
