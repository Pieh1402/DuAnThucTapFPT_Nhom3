<template>
  <v-container>
    <v-card>
      <v-card-title>Phản hồi hồ sơ</v-card-title>
      <v-form>
        <v-text-field label="Mã hồ sơ" v-model="form.id" required></v-text-field>
        <v-file-input label="Chọn hồ sơ bổ sung" v-model="form.file" required></v-file-input>
        <v-textarea label="Ghi chú" v-model="form.note"></v-textarea>
        <v-btn type="submit" color="primary">Gửi hồ sơ</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      form: {
        id: '',
        file: null,
        note: '',
      },
    };
  },
  methods: {
    async submitForm() {
      const formData = new FormData();
      formData.append('id', this.form.id);
      formData.append('file', this.form.file);
      formData.append('note', this.form.note);

      await fetch('/api/submit-response', {
        method: 'POST',
        body: formData,
      });
    },
  },
};
</script>
