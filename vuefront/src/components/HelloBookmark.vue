<template>
    <el-row :gutter="20">
        <el-col :xs="8" :sm="6" :md="6" :lg="4" :xl="4" v-for="(uu, index) in bookmarks" :key="index">
            <a :href="uu.url" target="_blank">
                <img :src="uu.ico" :alt="uu.title" />
                <span>{{ uu.title }}</span>
            </a>
        </el-col>
    </el-row>
</template>

<script>
import { mapState } from "vuex"
export default {
  name: "Bookmarks",
  inject: ['reload'],
  data() {
    return {
      dialogVisible: false,
      form: {
          content: "",
          category: '',
          dynamicTags: ['ABC', 'Hello World'],
          inputVisible: false,
          inputValue: ''
        }
    };
  },
  computed: mapState({
    bookmarks: state => state.bookmarks,
    category: state => state.category
  }),
  methods: 
    {
      addBookmark(item){
        this.$store.dispatch("addBookmark",item)
      },
      patchBookmark(pk, item){
        this.$store.dispatch("patchBookmark",pk, item)
        this.reload()
      },
      deleteBookmark(pk){
        this.$store.dispatch("deleteBookmark",pk)
      },
      handleClose(tag) {
        this.form.dynamicTags.splice(this.form.dynamicTags.indexOf(tag), 1);
      },
      showInput() {
        this.form.inputVisible = true;
        this.$nextTick(_ => {
          this.$refs.saveTagInput.$refs.input.focus();
        });
      },
      handleInputConfirm() {
        let inputValue = this.form.inputValue;
        if (inputValue) {
          this.form.dynamicTags.push(inputValue);
        }
        this.form.inputVisible = false;
        this.form.inputValue = '';
      },
      handleDataClose(done) {
        this.reload()
      }
    },
    created() {
    this.$store.dispatch("getBookmarks"),
    this.$store.dispatch("getCategory")
      },
};
</script>

<style scoped lang="scss">
a {
    display: block;
    padding: 0.5rem 0 0.5rem 1rem;
    margin-bottom: 1rem;
    color: #444d58;
}
a:-webkit-any-link {
    color: none;
    cursor: pointer;
    text-decoration: none;
}
a:hover {
    box-shadow: 0 2px 6px rgba(92, 88, 88, 0.175);
}
a,
a:focus,
a:hover {
    text-decoration: none;
}
img {
    width: 1.2rem;
    margin: 0 0.2rem -0.1rem 0;
}

.tags{
  margin-right: 10px;
  margin-bottom: 5px;
}
.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>