<template>
  <v-container class="py-10">
    <v-card elevation="3" class="pa-6 rounded-xl">
      <v-row align="center" justify="space-between">
        <v-col cols="12" md="7">
          <h1 class="text-h4 font-weight-bold mb-4">
            Giới thiệu về Đăng ký Doanh nghiệp
          </h1>
          <p class="mb-4">
            Đăng ký doanh nghiệp là bước đầu tiên và quan trọng nhất để hợp pháp
            hóa hoạt động kinh doanh tại Việt Nam. Thủ tục này giúp xác nhận tư
            cách pháp lý và bảo vệ quyền lợi của doanh nghiệp.
          </p>
          <p class="mb-4">
            Theo Luật Doanh nghiệp 2020, mọi tổ chức, cá nhân đều có quyền thành
            lập doanh nghiệp, trừ các trường hợp bị cấm. Việc đăng ký có thể
            thực hiện trực tiếp hoặc qua cổng thông tin điện tử quốc gia.
          </p>
          <v-btn
            color="primary"
            class="mt-4"
            href="https://dangkykinhdoanh.gov.vn/"
            target="_blank"
          >
            Đăng ký tại Cổng thông tin quốc gia
          </v-btn>
        </v-col>

        <v-col cols="12" md="5">
          <v-img
            src="https://cdn.thuvienphapluat.vn/uploads/tintuc/2021/09/08/dang-ky-doanh-nghiep.jpg"
            alt="Đăng ký doanh nghiệp"
            cover
            class="rounded-lg"
            height="300"
          />
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
// Không cần xử lý logic trong component này
</script>

<style scoped>
p {
  line-height: 1.6;
  font-size: 16px;
}
</style>
