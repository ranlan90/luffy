<template>
  <div class="footer" v-show="!$route.meta.hide">
    <div class="footer_div">
      <div class="logo_other_site_div">
        <img class="logo_img"
             src="">
        <p class="logo_other_site_description_p">马上入门，轻松学IT</p>
      </div>
      <div class="category_div company_description">
        <p class="main_category">公司</p>
        <a href="" class="single_item_a">
          关于我们
        </a>
        <a href="" class="single_item_a">
          加入我们
        </a>
      </div>
      <div class="category_div cooperation_div">
        <p class="main_category">合作</p>
        <a href="" class="single_item_a">
          我要投稿
        </a>
        <a href="" class="single_item_a">
          教师合作
        </a>
        <a href="" class="single_item_a">
          开发者
        </a>

      </div>
      <div class="category_div service_div">
        <p class="main_category">服务</p>
        <a href="" class="single_item_a">
          常见问题
        </a><a href="" class="single_item_a">
          隐私条款
        </a>
      </div>
      <div class="category_div learning_path_div">
        <p class="main_category">学习路径</p>
        <a href="" class="single_item_a">
          Python学习路径
        </a>
        <a href="" class="single_item_a">
          Linux学习路径
        </a>
        <a href="" class="single_item_a">
          Vue学习路径
        </a>
      </div>
    </div>
    <div class="site_information">
      Copyright @2013-2019
    </div>
  </div>
</template>

<script type="text/javascript">
  export default {}
</script>

<style type="text/css" scoped>
  .footer {
    background: #333;
    padding-top: 20px;
  }

  .footer_div {
    width: 1170px;
    margin: 0 auto;
    padding: 0 15px;
    display: flex;
    position: relative;
  }

  /* */
  .logo_other_site_div {
    width: 33.333333%;
  }

  .logo_img {
    height: auto;
    padding: 15px;
  }

  .logo_other_site_description_p {
    margin: 0 0 12px 15px;
    color: #0c9;
    font-size: 28px;
  }

  /* */
  .main_category {
    font-size: 18px;
    margin-bottom: 10px;
    color: hsla(0, 0%, 100%, .5);
  }

  .category_div {
    width: 16.66666%;
    padding: 0 15px;
    display: flex;
    flex-direction: column;
  }

  .single_item_a {
    display: inline-block;
    color: #999;
    font-size: 14px;
    margin-bottom: 3px;
  }

  .single_item_a:hover {
    color: #fff;
  }

  /* 网站信息部分，备案等 */

  .site_information {
    background: #171919;
    box-sizing: border-box;
    margin-top: 20px;
    height: 50px;
    text-align: center;
    color: #666;
    line-height: 50px;
  }


</style>
