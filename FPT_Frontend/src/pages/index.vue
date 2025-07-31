<template>
  <Status />
</template>

<script setup>
import { onMounted } from "vue";
import SubmitApplication from "./SubmitApplication.vue";
import Status from "./Status.vue";
const router = useRouter();

onMounted(() => {
  const token = localStorage.getItem("token");
  if (!token) {
    router.replace("/Login"); // chỉ chuyển nếu chưa login
  }
});
</script>
<style scoped></style>
