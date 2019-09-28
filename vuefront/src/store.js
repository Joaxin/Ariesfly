import Vue from "vue";
import Vuex from "vuex";
import uuService from "@/services/uuService";

Vue.use(Vuex);

export default new Vuex.Store({
  namespaced: true,
  state: {
    bookmarks: [],
    category: [],
  },
  getters: {
    bookmarks: state => {
      return state.bookmarks;
    },
    category: state => {
      return state.category;
    },
  },
  mutations: {
    setBookmarks(state, bookmarks) {
      state.bookmarks = bookmarks;
    },
    addBookmark(state, bookmark) {
      state.bookmarks.push(bookmark);
    },
    patchBookmark(state, msgId, bookmarks) {
      state.bookmarks = state.bookmarks.splice(msgId, 1, bookmarks);
      state.bookmarks = bookmarks;
    },
    deleteBookmark(state, msgId) {
      state.bookmarks = state.bookmarks.filter(obj => obj.id !== msgId);
    },
    setCategory(state, category) {
      state.category = category;
    },

  },
  actions: {
    getBookmarks({ commit }) {
      uuService.fetchBookmarks().then(bookmarks => {
        commit("setBookmarks", bookmarks);
      });
    },
    addBookmark({ commit }, bookmark) {
      uuService.postBookmark(bookmark).then(() => {
        commit("addBookmark", bookmark);
      });
    },
    patchBookmark({ commit }, msgId, bookmark) {
      uuService.patchBookmark(msgId, bookmark);
      commit("patchBookmark", msgId, bookmark);
    },
    deleteBookmark({ commit }, msgId) {
      uuService.deleteBookmark(msgId);
      commit("deleteBookmark", msgId);
    },
    getCategory({ commit }) {
      uuService.fetchCategory().then(category => {
        commit("setCategory", category);
      });
    },
  }
});