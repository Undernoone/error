<template>
<!--  首页底部  -->
  <div class="footer-view">
    <div class="foot-link-box flex-view">
      <a href="https://github.com/Undernoonep" class="foot-link" target="_blank">系统文档</a>
      <div class="link-split"></div>
      <a href="/#/admin" class="foot-link" target="_blank">后台管理</a>
      <div class="link-split"></div>
      <a href="https://github.com/Undernoone" class="foot-link" target="_blank">关于我们</a>
    </div>
    <div class="footer-infos">
      <span>
        <a style="color: rgb(255,0,0);">长ICP备20020729号</a>
      </span>
      <span>&nbsp;&nbsp;长公网安备2024&nbsp;&nbsp;新出发长零字第东0729号&nbsp;&nbsp;统一社会信用代码20020728</span>
    </div>
    <div class="address">2023-2024 © 长春代码演示 · All Rights Reserved</div>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  data () {
    return {}
  },
  methods: {}
}
</script>

<style scoped lang="less">
.flex-view {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.footer-view {
  max-width: 1108px;
  margin: 0 auto;
  padding: 24px 0 20px 54px;

  .foot-link-box {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    overflow: hidden;
    margin: 24px auto 16px;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
    .foot-link {
      margin: 0 16px;
      color: #ff0000;
    }
    a {
      background-color: transparent;
      text-decoration: none;
      color: var(--mid-blue);
    }
  }
  .footer-infos {
    height: 16px;
    line-height: 16px;
    font-size: 12px;
    padding-left: 63px;
    color: #ff0000;
    margin-top: 16px;
    text-align: center;
  }

  .footer-infos {
    height: 16px;
    line-height: 16px;
    font-size: 12px;
    padding-left: 63px;
    color: #ff0000;
    margin-top: 16px;
    text-align: center;
  }
  .address {
    text-align: center;
    height: 16px;
    line-height: 16px;
    font-size: 12px;
    color: #ff0000;
    margin-top: 8px;
  }
}
</style>
