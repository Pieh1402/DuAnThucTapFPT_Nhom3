<route lang="yaml">
meta:
  layout: login
</route>
<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const container = ref<HTMLElement | null>(null);

const email = ref("");
const password = ref("");
const error = ref("");

// Biến cho form đăng ký
const companyName = ref("");
const registerEmail = ref("");
const phone = ref("");
const registerPassword = ref("");
const registerError = ref("");

// Toggle giữa Sign In / Sign Up
onMounted(() => {
  const registerBtn = document.getElementById("register");
  const loginBtn = document.getElementById("login");

  registerBtn?.addEventListener("click", () => {
    container.value?.classList.add("active");
  });

  loginBtn?.addEventListener("click", () => {
    container.value?.classList.remove("active");
  });
});
const handleRegister = async () => {
  try {
    const res = await axios.post(
      "http://127.0.0.1:8000/api/auth/register",
      {
        company_name: companyName.value,
        email: registerEmail.value,
        phone: phone.value,
        password: registerPassword.value,
      },
      { headers: { "Content-Type": "application/json" } }
    );
    alert(res.data.message || "Đăng ký thành công!");
    registerError.value = "";
    container.value?.classList.remove("active"); // Quay về trang đăng nhập
  } catch (err) {
    const e = err as any;
    registerError.value = e.response?.data?.message || "Đăng ký thất bại!";
  }
};
// Xử lý đăng nhập
const handleLogin = async () => {
  try {
    const res = await axios.post(
      "http://127.0.0.1:8000/api/auth/login",
      {
        email: email.value,
        password: password.value,
      },
      { headers: { "Content-Type": "application/json-patch+json" } }
    );

    localStorage.setItem("token", res.data.access_token);
    localStorage.setItem("role", res.data.role);
    router.push("/");
  } catch (err) {
    const e = err as any;
    error.value = e.response?.data?.errors
      ? JSON.stringify(e.response.data.errors)
      : "Đăng nhập thất bại!";
  }
};
</script>

<template>
  <div class="login-page">
    <div class="container" id="container" ref="container">
      <!-- Sign Up -->
      <div class="form-container sign-up">
        <form @submit.prevent="handleRegister">
          <h1>Create Account</h1>
          <span>or use your email for registration</span>
          <input type="text" v-model="companyName" placeholder="Company Name" />
          <input type="email" v-model="registerEmail" placeholder="Email" />
          <input type="text" v-model="phone" placeholder="Phone" />
          <input
            type="password"
            v-model="registerPassword"
            placeholder="Password"
          />
          <button type="submit">Sign up</button>
          <p v-if="registerError" style="color: red; margin-top: 10px">
            {{ registerError }}
          </p>
        </form>
      </div>

      <!-- Sign In -->
      <div class="form-container sign-in">
        <form @submit.prevent="handleLogin">
          <h1>Sign In</h1>
          <div class="social-icons">
            <a href="#" class="icon"
              ><i class="fa-brands fa-google-plus-g"></i
            ></a>
            <a href="#" class="icon"><i class="fa-brands fa-github"></i></a>
            <a href="#" class="icon"><i class="fa-brands fa-facebook"></i></a>
            <a href="#" class="icon"
              ><i class="fa-brands fa-linkedin-in"></i
            ></a>
          </div>
          <span>or use your email for login</span>
          <input type="email" v-model="email" placeholder="Email" />
          <input type="password" v-model="password" placeholder="Password" />
          <a href="#">Forget Your password</a>
          <button type="submit">Sign in</button>
          <p v-if="error" style="color: red; margin-top: 10px">{{ error }}</p>
        </form>
      </div>

      <!-- Toggle Panels -->
      <div class="toggle-contaier">
        <div class="toggle">
          <div class="toggle-panel toggle-left">
            <h1>Welcome Back!</h1>
            <p>Lorem ipsum dolor sit amet consectetur.</p>
            <button class="hidden" id="login">Sign in</button>
          </div>
          <div class="toggle-panel toggle-right">
            <h1>Hello Friend</h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
            <button class="hidden" id="register">Sign up</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped></style>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.login-page {
  background: linear-gradient(135deg, #cecee6, #2501a5);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  height: 100vh;
}

.container {
  background-color: #fff;
  border-radius: 30px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.35);
  position: relative;
  overflow: hidden;
  width: 768px;
  max-width: 100%;
  min-height: 480px;
}

.container p {
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.3px;
  margin: 20px 0;
}

.container span {
  font-size: 12px;
}

.container a {
  color: #ccc;
  font-size: 13px;
  text-decoration: none;
  margin: 15px 0 10px;
}

.container button {
  background-color: #2501a5;
  color: #fff;
  font-size: 12px;
  padding: 10px 45px;
  border: 1px solid transparent;
  border-radius: 8px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-top: 10px;
  cursor: pointer;
}

.container button.hidden {
  background-color: transparent;
  border-color: #fff;
}

.container form {
  background-color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 40px;
  height: 100%;
}

.container input {
  background-color: #eee;
  border: none;
  margin: 8px 0;
  padding: 10px 15px;
  font-size: 13px;
  border-radius: 8px;
  width: 100%;
  outline: none;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}
.sign-in {
  left: 0;
  width: 50%;
  z-index: 2;
}

.container.active .sign-in {
  transform: translateX(100%);
}
.sign-up {
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}

.container.active .sign-up {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: move 0.6s;
}

@keyframes move {
  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }
  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
}

.social-icons {
  margin: 20px 0;
}

.social-icons a {
  color: black;
  border: 1px solid #ccc;
  border-radius: 20%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 0 3px;
  width: 40px;
  height: 40px;
}

.toggle-contaier {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: all 0.6s ease-in-out;
  border-radius: 150px 0 0 100px;
  z-index: 1000;
}

.container.active .toggle-contaier {
  transform: translateX(-100%);
  border-radius: 0 150px 100px 0;
}
.toggle {
  background-color: #2501a5;
  height: 100%;
  color: #fff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: all 0.6s ease-in-out;
}

.container.active .toggle {
  transform: translateX(50%);
}

.toggle-panel {
  position: absolute;
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 30px;
  text-align: center;
  top: 0;
  transform: translateX(0);
  transition: all 0.6s ease-in-out;
}

.toggle-left {
  transform: translateX(-200%);
}

.container.active .toggle-left {
  transform: translateX(0);
}

.toggle-right {
  right: 0;
  transform: translateX(0);
}

.container.active .toggle-right {
  transform: translateX(200%);
}
</style>
