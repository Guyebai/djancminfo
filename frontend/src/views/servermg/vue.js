vue.js
	是一套用于构建用户界面的渐进式框架。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动


	特点  
	1、确实轻量
	2、数据绑定
	3、指令
	4、插件化

vue.js与其他框架的区别
1、与AngularJS区别
    AngularJS来自于谷歌
    相同点：
	    都支持指令   内置指令和自定义指令
	    都支持过滤器   内置过滤器和自定义过滤器
	    都支持双向绑定
	    都不支持低端的浏览器（比如IE6 IE7  IE8）
	    	vue.js使用比如Array.isArray 的ES5特性
	     	AngularJS1.3开始不支持IE8
	不同点：
		AngularJS  学习成本高 Vue.js提供的API学习比较简单
		性能上


2、数据绑定
	2.1语法
	2.1.1 插值
	  文本插值是最基本的形式，使用双大括号{{}}
	  <span >Text:{{text}}</span>




	  for循环
	  <div id="ul_trans1">
        <ul >交通工具
            <li v-for="tab in tabs">{{ tab.name }}</li>

        </ul>
    </div>
    <span id="spantext">Text:{{text}}</span>

      Js代码
		      <script >
		 var  Tab =   new  Vue ({
		    el:'#ul_trans1',
		    data:{
		    tabs:[
		    {name:"公交"},
		    {name:"火车"},
		    {name:"轮船"},
		    {name:"飞机"},
		    {name:"地铁"}

		    ]
			}
			})

			</script>

	  Tab.tabs.push({ name: '新项目3' })

v-model  装饰

v-model.lazy= ""   lazy惰性更新  不会实时更新
v-model.trim=""    去掉前后输入的空格
v-model.number=""    输入的内容为数字

v-model在其他元素或者类型上的使用
1、input
	radio   单选框
	checkout  多选框
2、textarea

3、select  selected
MVVM模式其自身是实现了数据的双向绑定的，在Vue.js中我们可以通过指令v-model来实现数据双向绑定


vue组件的基本步骤
1、创建组件构造器
let  Profile =Vue.extend({
//1.1 模板选项
template:·<div>
	<input type='date'>
	<p>今天已经是冬天了</p>

</div>·
	
}
)








