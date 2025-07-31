<template>
  <v-container>
    <v-row>

        <div>
            <h2>
              Thống kê tháng 4/2025 về <br>
              Đăng ký doanh nghiệp
            </h2>
        </div>

      <v-col>
          <div style="margin-left: 100px; font-size: 20px;">
            <p class="highlight-text">Tổng doanh nghiệp thành lập mới: 15.228</p>
            <p class="highlight-text">Doanh nghiệp quay trở lại hoạt động: 9.104</p>
            <p class="highlight-text">Doanh nghiệp giải thể: 1.750</p>
            <p class="highlight-text">Doanh nghiệp tạm ngưng hoạt động: 5.924</p>
          </div>
      </v-col>
    </v-row>
    <div style="display: flex; gap: 16px;">
        <div class="title">
          <img src="https://media.istockphoto.com/id/962564820/vi/vec-to/d%E1%BA%A5u-ch%E1%BA%A5m-than-trong-bi%E1%BB%83u-t%C6%B0%E1%BB%A3ng-vector-gi%E1%BB%8Dng-n%C3%B3i-bong-b%C3%B3ng-kh%C3%A1i-ni%E1%BB%87m-os-ch%C3%BA-%C3%BD-ho%E1%BA%B7c-d%E1%BA%A5u-hi%E1%BB%87u.jpg?s=612x612&w=0&k=20&c=Xmht7NABumBXkAbk44x7JemX71QMIgctR0hWVJYFML0=">
          <p>Dịch vụ thông tin</p>
        </div>
        <div class="title">
          <img src="https://clc.hust.edu.vn/xmedia/2021/03/form-dang-ky-aptis-minh-hoa.png">
          <p>Đăng ký doanh nghiệp</p>
        </div>
        <div class="title">
          <img src="https://png.pngtree.com/png-vector/20190629/ourlarge/pngtree-reports-icon-for-your-project-png-image_1521526.jpg">
          <p>Báo cáo điện tử</p>
        </div>
        <div class="title">
          <img src="https://i-law.vn/uploads/articles/68399/ho_kinh_doanh_la_gi_2702164641.png">
          <p>Đăng ký hộ kinh doanh</p>
        </div>
        <div class="title">
          <img src="https://img.pikbest.com/png-images/qiantu/business-handshake-icon_2678293.png!sw800">
          <p>Đăng ký hợp tác xã</p>
        </div>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'HomePage',
}
</script>
<style>
.highlight-text {
  background-color: #1cd4d4;
  padding: 12px 16px;
  border-radius: 8px;
  color: #ffffff;
  margin-top: 5px;
  margin-bottom: 5px;
}
.title{
  text-align: center;
  background-color: gray;
  padding: 12px;
  border-radius: 10px;
  width: 230px;
}
img{
  width: 200px;
  height: 200px;
  border-radius: 10px;
}
p{
  color: white;
  padding: 6px;
  margin-top: 6px;
}
</style>