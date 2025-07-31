<template>
  <v-app>
    <!-- Header Services Bar -->
    <v-app-bar
      class="header-services"
      elevation="4"
      height="180"
      color="primary"
    >
      <v-container>
        <v-row justify="center" align="center" class="fill-height">
          <v-col
            v-for="service in headerServices"
            :key="service.id"
            cols="auto"
            class="text-center"
          >
            <v-card
              class="header-item pa-4 mx-3"
              color="rgba(255,255,255,0.15)"
              variant="flat"
              rounded="xl"
              @click="handleHeaderServiceClick(service)"
              hover
              min-height="120"
            >
              <v-avatar size="70" class="mb-3" color="white">
                <v-icon size="35" :color="service.iconColor">
                  {{ service.icon }}
                </v-icon>
              </v-avatar>
              <v-card-text class="pa-2">
                <div
                  class="text-body-2 font-weight-bold text-white text-uppercase text-center"
                  style="line-height: 1.3"
                >
                  {{ service.title }}
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>

    <!-- Main Content -->
    <v-main class="gradient-bg" style="margin-top: 180px">
      <v-container class="py-12">
        <v-row>
          <!-- Services Grid -->
          <v-col cols="12" lg="8">
            <v-row>
              <v-col
                v-for="(service, index) in mainServices"
                :key="service.id"
                cols="12"
                sm="6"
                md="4"
              >
                <v-card
                  :class="[
                    'service-card',
                    'pa-6',
                    'text-center',
                    { pulse: index === 0 },
                  ]"
                  elevation="8"
                  rounded="xl"
                  @click="handleServiceClick(service)"
                  hover
                >
                  <v-avatar
                    size="80"
                    class="service-icon mb-4"
                    :style="{ background: service.gradient }"
                  >
                    <v-icon size="40" color="white">{{ service.icon }}</v-icon>
                  </v-avatar>

                  <v-card-title
                    class="text-h6 font-weight-bold text-center pa-0"
                  >
                    {{ service.title }}
                  </v-card-title>
                </v-card>
              </v-col>
            </v-row>
          </v-col>

          <!-- Sidebar -->
          <v-col cols="12" lg="4">
            <v-card class="pa-6" elevation="8" rounded="xl" sticky>
              <v-card-title
                class="text-h6 font-weight-bold white--text pa-4 ma-n6 mb-6 support-header"
              >
                <v-icon left color="white">mdi-help-circle</v-icon>
                THÔNG TIN HỖ TRỢ
              </v-card-title>

              <v-card-text class="pa-0">
                <div class="mb-4">
                  <h4 class="font-weight-bold mb-2">
                    Cơ quan tiếp nhận phản ánh, kiến nghị
                  </h4>
                  <p class="text-body-2 mb-0">
                    Cơ quan đăng ký kinh doanh cấp tỉnh (đối với doanh nghiệp),
                    cơ quan đăng ký kinh doanh cấp xã (đối với hợp tác xã, hộ
                    kinh doanh).
                  </p>
                </div>

                <div class="mb-4">
                  <h4 class="font-weight-bold mb-2">Hộp thư hỗ trợ</h4>
                  <p class="text-body-2 mb-2">
                    Đăng ký doanh nghiệp trực tuyến
                  </p>
                  <p class="font-weight-bold text-primary">ĐT: 024.3726.0413</p>
                </div>

                <v-card
                  class="pa-4 contact-card"
                  color="grey-lighten-4"
                  rounded="lg"
                  flat
                >
                  <v-list-item class="pa-0">
                    <template #prepend>
                      <v-icon color="#00ACC1">mdi-email</v-icon>
                    </template>
                    <v-list-item-content>
                      <v-list-item-title class="text-body-2">
                        hotro@dangkykinhoanh.gov.vn
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>

    <!-- Snackbar for notifications -->
    <v-snackbar
      v-model="snackbar.show"
      :color="snackbar.color"
      :timeout="3000"
      top
      right
    >
      {{ snackbar.message }}
      <template #actions>
        <v-btn color="white" variant="text" @click="snackbar.show = false">
          Đóng
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script>
export default {
  name: "GovernmentServicesPortal",

  data() {
    return {
      snackbar: {
        show: false,
        message: "",
        color: "success",
      },

      headerServices: [
        {
          id: 1,
          title: "Dịch vụ thông tin",
          icon: "mdi-information",
          iconColor: "#1976D2", // Blue
        },
        {
          id: 2,
          title: "Đăng ký doanh nghiệp",
          icon: "mdi-clipboard-text",
          iconColor: "#00ACC1", // Cyan
        },
        {
          id: 3,
          title: "Bộ cáo điện tử",
          icon: "mdi-email-open",
          iconColor: "#0277BD", // Light Blue
        },
        {
          id: 4,
          title: "Đăng ký hộ kinh doanh",
          icon: "mdi-chart-line",
          iconColor: "#26A69A", // Teal
        },
        {
          id: 5,
          title: "Đăng ký hợp tác xã",
          icon: "mdi-handshake",
          iconColor: "#0288D1", // Light Blue Darken
        },
      ],

      mainServices: [
        {
          id: 1,
          title: "Hướng dẫn sử dụng dịch vụ công",
          icon: "mdi-laptop",
          gradient: "linear-gradient(135deg, #1976D2 0%, #2196F3 100%)", // Blue gradient
          url: "https://dangkykinhdoanh.gov.vn/vn/Pages/Huongdansudungdvc.aspx"
        },
        {
          id: 2,
          title: "Hướng dẫn đăng ký doanh nghiệp",
          icon: "mdi-file-document",
          gradient: "linear-gradient(135deg, #00ACC1 0%, #26C6DA 100%)", // Cyan gradient
        },
        {
          id: 3,
          title: "Tra cứu nhãn hiệu, chỉ dẫn địa lý được bảo hộ sở hữu trí tuệ",
          icon: "mdi-magnify",
          gradient: "linear-gradient(135deg, #0277BD 0%, #039BE5 100%)", // Light Blue gradient
          url: "https://dangkykinhdoanh.gov.vn/vn/Pages/noipsearch.aspx"
        },
        {
          id: 4,
          title: "Ngành nghề đầu tư kinh doanh có điều kiện",
          icon: "mdi-gavel",
          gradient: "linear-gradient(135deg, #26A69A 0%, #4DB6AC 100%)", // Teal gradient
          url: "https://dangkykinhdoanh.gov.vn/vn/Pages/Nganhnghedautukinhdoanh.aspx"
        },
        {
          id: 5,
          title: "Điều kiện đầu tư kinh doanh đối với nhà đầu tư nước ngoài",
          icon: "mdi-earth",
          gradient: "linear-gradient(135deg, #0288D1 0%, #29B6F6 100%)", // Light Blue Darken gradient
          url: "https://dautunuocngoai.gov.vn/fdi/nganhnghedautu/6"
        },
        {
          id: 6,
          title: "Thông tin về quản tài viên",
          icon: "mdi-account-tie",
          gradient: "linear-gradient(135deg, #1565C0 0%, #1976D2 100%)", // Blue Darken gradient
          url: "https://bttp.moj.gov.vn/qt/tintuc/Pages/quan-tai-vien.aspx"
        },
      ],
    };
  },

  methods: {
    handleHeaderServiceClick(service) {
      this.showNotification(`Bạn đã chọn: ${service.title}`, "info");
      // Implement navigation logic here
      console.log("Header service clicked:", service);
    },

    handleServiceClick(service) {
      this.showNotification(`Đang mở: ${service.title}`, "success");
      // Implement service logic here
      console.log("Service clicked:", service);
      if (service.url) {
        window.open(service.url, "_blank"); // Mở trang trong tab mới
      }
    },

    showNotification(message, color = "success") {
      this.snackbar = {
        show: true,
        message,
        color,
      };
    },
  },
};
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(135deg, #1976d2 0%, #2196f3 50%, #00bcd4 100%);
  min-height: 100vh;
}

.header-services {
  background: linear-gradient(
    90deg,
    #1565c0 0%,
    #1976d2 50%,
    #2196f3 100%
  ) !important;
}

.service-card {
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
  cursor: pointer;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15) !important;
}

.header-item {
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.header-item:hover {
  transform: translateY(-3px);
  background: rgba(255, 255, 255, 0.25) !important;
}

.support-header {
  background: linear-gradient(135deg, #26a69a, #00acc1) !important;
  border-radius: 12px 12px 0 0 !important;
}

.contact-card {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
  border: 1px solid rgba(0, 172, 193, 0.2);
}

.pulse {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(25, 118, 210, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(25, 118, 210, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(25, 118, 210, 0);
  }
}

/* Responsive adjustments */
@media (max-width: 960px) {
  .header-item {
    margin: 0 4px !important;
  }
}

@media (max-width: 600px) {
  .header-item .v-card-text div {
    font-size: 10px !important;
  }

  .header-item .v-avatar {
    width: 50px !important;
    height: 50px !important;
  }
}
</style>
