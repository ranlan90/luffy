<template>
  <div class="box">
    <div class="login">
      <div class="login-title">
        <!--				<img src="https://www.luffycity.com/static/img/Logotitle.1ba5466.png" alt="">-->
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <div class="title">
          <span>注册</span>
        </div>
        <div class="inp">
          <input v-model='username' type="text" placeholder="用户名 / 手机号码" class="user">
          <input v-model='email' type="text" name="" class="pwd" placeholder="邮箱" style="margin-top:20px ">

          <input v-model='password' type="password" name="" class="pwd" placeholder="密码" style="margin-top:20px ">
          <input v-model='re_password' type="password" name="" class="pwd" placeholder="重复密码" style="margin-top:20px ">
          <button class="login_btn" @click='regHandler'>注册</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Register',
    data() {
      return {
        username: "",
        password: "",
        email: "",
        re_password: "",
      }
    },

    methods: {
      regHandler() {
        let params = {
          username: this.username,
          password: this.password,
          re_password: this.re_password,
          email: this.email,
        }
        this.$http.userReg(params)
          .then(res => {
            console.log("hell")
            console.log(res)
            if (res.data.code == 1000) {
              // this.$router.go(-1)
              this.$router.push({
                name: "Login"
              });


            } else {
              this.$message('注册失败')
            }
          })
          .catch(err => {
            console.log(err);
          })
      },
    },
  };
</script>

<style lang="css" scoped>
  .box {
    /*width: 100%;*/
    /*position: relative;*/
    width: 1170px;
    padding: 0 30px;
    margin: auto;
    background: #fff;

  }

  .box img {
    width: 100%;
  }

  .box .login {
    position: absolute;
    width: 500px;
    height: 400px;
    top: 50%;
    left: 50%;
    margin-left: -250px;
    margin-top: -300px;
  }

  .login .login-title {
    width: 100%;
    text-align: center;
  }

  .login-title img {
    width: 190px;
    height: auto;
  }

  .login-title p {
    font-family: PingFangSC-Regular;
    font-size: 18px;
    color: #fff;
    letter-spacing: .29px;
    padding-top: 10px;
    padding-bottom: 50px;
  }

  .login_box {
    width: 400px;
    height: auto;
    background: #fff;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .5);
    border-radius: 4px;
    margin: 0 auto;
    padding-bottom: 40px;
  }

  .login_box .title {
    font-size: 20px;
    color: #9b9b9b;
    letter-spacing: .32px;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-around;
    padding: 50px 60px 0 60px;
    margin-bottom: 20px;
    cursor: pointer;
  }

  .login_box .title span:nth-of-type(1) {
    color: #4a4a4a;
    border-bottom: 2px solid #84cc39;
  }

  .inp {
    width: 350px;
    margin: 0 auto;
  }

  .inp input {
    border: 0;
    outline: 0;
    width: 100%;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
  }

  .inp input.user {
    margin-bottom: 4px;
  }

  .inp .rember {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
  }

  .inp .rember p:first-of-type {
    font-size: 12px;
    color: #4a4a4a;
    letter-spacing: .19px;
    margin-left: 22px;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    /*position: relative;*/
  }

  .inp .rember p:nth-of-type(2) {
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
  }

  .inp .rember input {
    outline: 0;
    width: 30px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
  }

  .inp .rember p span {
    display: inline-block;
    font-size: 12px;
    width: 100px;
    /*position: absolute;*/
    /*left: 20px;*/

  }

  #geetest {
    margin-top: 20px;
  }

  .login_btn {
    width: 100%;
    height: 45px;
    background: #84cc39;
    border-radius: 5px;
    font-size: 16px;
    color: #fff;
    letter-spacing: .26px;
    margin-top: 30px;
  }

  .inp .go_login {
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
  }

  .inp .go_login span {
    color: #84cc39;
    cursor: pointer;
  }
</style>
