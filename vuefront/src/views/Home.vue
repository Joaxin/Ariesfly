<template>
    <div>
        <el-row type="flex" class="row-bg" justify="center">
            <el-col :xs="20" :sm="16" :md="12" :lg="8" id="col-search">
                <HelloSearch/>
            </el-col>
        </el-row>
        <el-row type="flex" class="row-bg" justify="center" id="row-bookmark">
            <el-col :xs="24" :sm="20" :md="16" :lg="14" :xl="12" id="col-bookmark">
                <HelloBookmark/>
            </el-col>
        </el-row>
    </div>
</template>

<script>
// @ is an alias to /src
import HelloSearch from "@/components/HelloSearch.vue";
import HelloBookmark from "@/components/HelloBookmark.vue";

export default {
  name: "home",
  components: {
    HelloSearch,
    HelloBookmark
  }
};
</script>

<style scoped>
#col-search {
    margin-top: 10%;
}
#row-bookmark {
    padding-top: 4rem;
}
#col-bookmark {
    padding: 1rem .5rem .5rem .5rem;
    background: white;
    border-radius: 4px;
}
</style>>