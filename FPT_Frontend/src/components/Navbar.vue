<script lang="ts" setup>
import HoverMenu from "./HoverMenu.vue";
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const isAdmin = ref(false);
const router = useRouter();

onMounted(() => {
  isAdmin.value = localStorage.getItem('role') === 'admin';
});
</script>

<template>
  <v-app-bar app color="#1976d2" dark flat style="overflow: visible">
    <!-- Logo và tiêu đề -->
    <v-toolbar-title class="d-flex align-center">
      <v-icon class="mr-2">mdi-office-building</v-icon>
      <span class="font-weight-bold text-h6">ĐĂNG KÝ DOANH NGHIỆP</span>
    </v-toolbar-title>

    <v-spacer />

    <!-- Menu chính -->
    <div class="d-flex align-center">
      <router-link to="/NotFound">
        <HoverMenu title="Trang chủ" class="menu-btn" />
      </router-link>
      <router-link to="/Introduce">
        <HoverMenu title="Giới thiệu" class="menu-btn" />
      </router-link>
      <HoverMenu title="Dịch vụ công" class="menu-btn">
        <v-list class="pa-2" min-width="250">
          <router-link to="/SubmitApplication">
            <v-list-item link>
              <v-list-item-title>Đăng ký doanh nghiệp</v-list-item-title>
            </v-list-item>
          </router-link>
          <router-link to="/Status">
            <v-list-item link>
              <v-list-item-title>Xem trạng thái</v-list-item-title>
            </v-list-item>
          </router-link>
          <v-list-item link>
            <v-list-item-title>Giải thể doanh nghiệp</v-list-item-title>
          </v-list-item>
          <router-link to="NotFound">
            <v-list-item link>
              <v-list-item-title>Tạm ngừng hoạt động</v-list-item-title>
            </v-list-item>
          </router-link>
        </v-list>
      </HoverMenu>
      <HoverMenu title="Hỗ trợ" class="menu-btn">
        <v-list class="pa-2" min-width="200">
          <v-list-item link>
            <v-list-item-title>Hướng dẫn sử dụng</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title>Liên hệ</v-list-item-title>
          </v-list-item>
        </v-list>
      </HoverMenu>
      <HoverMenu title="Tin tức" class="menu-btn">
        <v-list class="pa-2" min-width="200">
          <v-list-item link>
            <v-list-item-title>Tin tức mới</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title>Thông báo</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title>Văn bản pháp luật</v-list-item-title>
          </v-list-item>
        </v-list>
      </HoverMenu>
      <HoverMenu title="Văn bản pháp luật" class="menu-btn">
        <v-list class="pa-2" min-width="220">
          <v-list-item link>
            <v-list-item-title>
              <a
                href="https://thuvienphapluat.vn/van-ban/Doanh-nghiep/Luat-Doanh-nghiep-so-59-2020-QH14-427301.aspx"
                target="_blank"
              >
                Luật Doanh nghiệp</a
              ></v-list-item-title
            >
          </v-list-item>
          <v-list-item link>
            <v-list-item-title>Nghị định hướng dẫn</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title>Thông tư quy định</v-list-item-title>
          </v-list-item>
        </v-list>
      </HoverMenu>
      <!-- Nút quản trị chỉ hiện với admin -->
      <v-btn v-if="isAdmin" color="red" class="ml-4" @click="router.push('/AdminPanel')">
        Quản trị hệ thống
      </v-btn>
    </div>

    <!-- Tìm kiếm và đăng nhập -->
    <v-spacer />
    <router-link to="/login">
      <div
        class="d-flex align-center"
        style="gap: 8px; flex-shrink: 0; min-width: 400px"
      >
        <!-- Ô tìm kiếm -->
        <v-text-field
          v-model="searchText"
          placeholder="Tìm kiếm..."
          prepend-inner-icon="mdi-magnify"
          variant="outlined"
          density="compact"
          hide-details
          class="search-field"
          style="width: 200px; flex-shrink: 0"
        />
        <!-- Đăng nhập -->
        <v-btn
          variant="outlined"
          color="white"
          class="text-white"
          size="small"
          style="min-width: 85px; flex-shrink: 0; height: 32px"
        >
          ĐĂNG XUẤT
        </v-btn>
      </div>
    </router-link>
  </v-app-bar>
</template>

<script lang="ts">
export default {
  data() {
    return {
      searchText: "",
    };
  },
};
</script>

<style scoped>
.v-app-bar {
  position: static !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.menu-btn {
  position: relative;
  font-weight: 500;
  margin: 0 12px;
  padding: 8px 16px;
  border-radius: 4px;
  transition: all 0.3s ease;
  color: white;
}

.menu-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.search-field :deep(.v-field) {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 20px;
}

.search-field :deep(.v-field__input) {
  color: #333;
  font-size: 14px;
}

.search-field :deep(.v-field__prepend-inner) {
  color: #666;
}

.text-blue {
  color: #1976d2 !important;
}
a {
  text-decoration: none;
  color: black;
}

/* Animation cho hover effect */
@keyframes slideUp {
  from {
    transform: translateY(2px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.menu-btn:hover {
  animation: slideUp 0.2s ease-out;
}

/* Responsive */
@media (max-width: 1200px) {
  .search-field {
    max-width: 180px !important;
    min-width: 150px !important;
  }
}

@media (max-width: 960px) {
  .menu-btn {
    margin: 0 8px;
    padding: 8px 12px;
    font-size: 14px;
  }

  .search-field {
    max-width: 140px !important;
    min-width: 120px !important;
  }
}
</style>
