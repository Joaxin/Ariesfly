import api from "@/services/api";

export default {
  fetchBookmarks() {
    return api.get(`uu/`).then(response => response.data);
  },
  postBookmark(payload) {
    return api.post(`uu/`, payload).then(response => response.data);
  },
  
  patchBookmark(msgId, payload) {
    return api.patch(`uu/${msgId}/`, payload)
      .then(response => response.data)
      .catch(e => { console.log(e) })
  },
  deleteBookmark(msgId) {
    return api.delete(`uu/${msgId}`).then(response => response.data);
  },
  fetchCategory() {
    return api.get(`category/`).then(response => response.data);
  },
}