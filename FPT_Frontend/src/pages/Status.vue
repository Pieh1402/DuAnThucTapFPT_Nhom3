<template>
  <v-container class="py-10">
    <v-card class="pa-6" elevation="3">
      <v-row align="center" justify="space-between">
        <v-col cols="12" md="8">
          <h2 class="text-h5 font-weight-bold mb-4">Trạng thái hồ sơ</h2>
          <v-list dense>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title class="font-weight-bold">
                  Mã hồ sơ:
                </v-list-item-title>
                <v-list-item-subtitle>{{ hoSo.maHoSo }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title class="font-weight-bold">
                  Ngày nộp:
                </v-list-item-title>
                <v-list-item-subtitle>{{ hoSo.ngayNop }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title class="font-weight-bold">
                  Trạng thái:
                </v-list-item-title>
                <v-list-item-subtitle>
                  <v-chip color="primary" text-color="white">
                    {{ hoSo.trangThai }}
                  </v-chip>
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-col>

        <v-col cols="12" md="4" class="text-center">
          <v-btn color="primary" @click="getTrangThaiHoSo">
            Cập nhật trạng thái
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { reactive } from "vue";
import axios from "axios";

// Reactive object hiển thị lên UI
const hoSo = reactive({
  trangThai: "Chưa có dữ liệu",
  ngayNop: "-",
  maHoSo: "-",
});

// Hàm gọi API và cập nhật trạng thái hồ sơ
const getTrangThaiHoSo = async () => {
  try {
    const token = localStorage.getItem("token");
    if (!token) {
      alert("Chưa đăng nhập!");
      return;
    }

    const res = await axios.get(
      "http://127.0.0.1:8000/api/admin/applications",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    if (res.data.length === 0) {
      alert("Không tìm thấy hồ sơ nào.");
      return;
    }

    // Giả sử chỉ lấy hồ sơ đầu tiên (có thể chỉnh lại sau)
    const data = res.data[0];
    hoSo.trangThai = data.status || "Không rõ";
    hoSo.ngayNop = new Date(data.created_at).toLocaleDateString("vi-VN");
    hoSo.maHoSo = `HS${new Date(data.created_at)
      .toISOString()
      .slice(0, 10)
      .replace(/-/g, "")}-${data.id}`;
  } catch (err) {
    const e = err as any;
    console.error("Lỗi khi gọi API:", e);
    alert(
      e.response?.data?.detail ||
        e.message ||
        "Lỗi không xác định. Kiểm tra console (F12)."
    );
  }
};
</script>

<style scoped>
.text-h5 {
  font-size: 24px;
}
</style>
