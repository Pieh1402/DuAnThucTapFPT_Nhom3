<template>
  <v-container>
    <v-card>
      <v-card-title>Trang quản trị hệ thống</v-card-title>
      <v-card-text>
        <v-tabs v-model="tab">
          <v-tab>Hồ sơ chờ duyệt</v-tab>
          <v-tab>Người dùng</v-tab>
          <v-tab>Thống kê</v-tab>
        </v-tabs>

        <div v-if="tab === 0">
          <!-- Danh sách hồ sơ chờ duyệt -->
          <v-data-table class="mt-4" :headers="headers" :items="hoSoList">
            <template #item.actions="{ item }">
              <v-btn color="success" size="small" @click="duyetHoSo(item)">Duyệt</v-btn>
              <v-btn class="ml-2" color="error" size="small" @click="xoaHoSo(item)">Xóa</v-btn>
            </template>
          </v-data-table>
        </div>
        <div v-else-if="tab === 1">
          <!-- Quản lý người dùng -->
          <v-data-table class="mt-4" :headers="userHeaders" :items="userList" />
        </div>
        <div v-else-if="tab === 2">
          <!-- Thống kê -->
          <v-row class="mt-4">
            <v-col cols="12" md="4">
              <v-card color="primary" dark>
                <v-card-title>Tổng số hồ sơ</v-card-title>
                <v-card-text class="text-h4">{{ stats.total_applications }}</v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="4">
              <v-card color="success" dark>
                <v-card-title>Tổng số người dùng</v-card-title>
                <v-card-text class="text-h4">{{ stats.total_users }}</v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="4">
              <v-card color="info" dark>
                <v-card-title>Hồ sơ theo trạng thái</v-card-title>
                <v-card-text>
                  <div v-for="(count, status) in stats.by_status" :key="status">
                    Trạng thái {{ status }}: <b>{{ count }}</b>
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()

  const tab = ref(0)
  const headers = [
    { text: 'ID', value: 'id' },
    { text: 'Tên hồ sơ', value: 'ten_ho_so' },
    { text: 'Ngày nộp', value: 'ngay_nop' },
    { text: 'Trạng thái', value: 'ten_trang_thai' },
    { text: 'Thao tác', value: 'actions', sortable: false },
  ]
  const hoSoList = ref([])

  const userHeaders = [
    { text: 'ID', value: 'id' },
    { text: 'Tên đăng nhập', value: 'ten_dang_nhap' },
    { text: 'Email', value: 'email' },
    { text: 'Số điện thoại', value: 'so_dien_thoai' },
    { text: 'Trạng thái', value: 'trang_thai' },
  ]
  const userList = ref([])

  const stats = ref({ total_applications: 0, total_users: 0, by_status: {} })

  const getToken = () => localStorage.getItem('token')

  const fetchHoSo = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/admin/applications', {
        headers: { Authorization: `Bearer ${getToken()}` },
      })
      hoSoList.value = res.data
    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert('Phiên đăng nhập hết hạn hoặc không hợp lệ, vui lòng đăng nhập lại!')
        localStorage.removeItem('token')
        localStorage.removeItem('role')
        router.replace('/Login')
      } else {
        alert('Không lấy được danh sách hồ sơ!')
      }
    }
  }

  const fetchUsers = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/admin/users', {
        headers: { Authorization: `Bearer ${getToken()}` },
      })
      userList.value = res.data
    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert('Phiên đăng nhập hết hạn hoặc không hợp lệ, vui lòng đăng nhập lại!')
        localStorage.removeItem('token')
        localStorage.removeItem('role')
        router.replace('/Login')
      } else {
        alert('Không lấy được danh sách user!')
      }
    }
  }

  const fetchStats = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/admin/stats', {
        headers: { Authorization: `Bearer ${getToken()}` },
      })
      stats.value = res.data
    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert('Phiên đăng nhập hết hạn hoặc không hợp lệ, vui lòng đăng nhập lại!')
        localStorage.removeItem('token')
        localStorage.removeItem('role')
        router.replace('/Login')
      } else {
        alert('Không lấy được thống kê!')
      }
    }
  }

  const duyetHoSo = async item => {
    try {
      await axios.put(`http://127.0.0.1:8000/api/admin/applications/${item.id}/approve`, {}, {
        headers: { Authorization: `Bearer ${getToken()}` },
      })
      alert('Duyệt hồ sơ thành công!')
      fetchHoSo()
      fetchStats()
    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert('Phiên đăng nhập hết hạn hoặc không hợp lệ, vui lòng đăng nhập lại!')
        localStorage.removeItem('token')
        localStorage.removeItem('role')
        router.replace('/Login')
      } else {
        alert('Lỗi khi duyệt hồ sơ!')
      }
    }
  }

  const tuChoiHoSo = async item => {
    try {
      await axios.put(`http://127.0.0.1:8000/api/admin/applications/${item.id}/reject`, {}, {
        headers: { Authorization: `Bearer ${getToken()}` },
      })
      alert('Từ chối hồ sơ thành công!')
      fetchHoSo()
      fetchStats()
    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert('Phiên đăng nhập hết hạn hoặc không hợp lệ, vui lòng đăng nhập lại!')
        localStorage.removeItem('token')
        localStorage.removeItem('role')
        router.replace('/Login')
      } else {
        alert('Lỗi khi từ chối hồ sơ!')
      }
    }
  }

  const xoaHoSo = async item => {
    if (!confirm('Bạn có chắc chắn muốn xóa hồ sơ này?')) return;
    try {
      await axios.delete(`http://127.0.0.1:8000/api/admin/applications/${item.id}`, {
        headers: { Authorization: `Bearer ${getToken()}` },
      })
      alert('Xóa hồ sơ thành công!')
      fetchHoSo()
      fetchStats()
    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert('Phiên đăng nhập hết hạn hoặc không hợp lệ, vui lòng đăng nhập lại!')
        localStorage.removeItem('token')
        localStorage.removeItem('role')
        router.replace('/Login')
      } else {
        alert('Lỗi khi xóa hồ sơ!')
      }
    }
  }

  onMounted(() => {
    const token = localStorage.getItem('token')
    const role = localStorage.getItem('role')
    if (!token || role !== 'admin') {
      alert('Bạn không có quyền truy cập trang này!')
      router.replace('/Login')
    } else {
      fetchHoSo()
      fetchUsers()
      fetchStats()
    }
  })
</script>
