head=open('head.html').read(); script=open('script.html').read()
B='''
<div class="sc"><div class="e big" data-a="0.3" data-b="4.3">لا أحد يبني سفينته…<br>والمطر يهطل</div>
 <div class="e big g" data-a="1.8" data-b="4.3" style="margin-top:24px">نوحٌ بناها…<br>والسماء صافية</div></div>

<div class="sc list"><div class="e mid" data-a="4.6" data-b="9.3">طوفانك قد لا يكون ماءً…</div>
 <div class="e g" style="font-size:58px;margin-top:20px" data-a="5.6" data-b="9.3">رزقٌ يضيق</div>
 <div class="e g" style="font-size:58px" data-a="6.4" data-b="9.3">خوفٌ من الغد</div>
 <div class="e g" style="font-size:58px" data-a="7.2" data-b="9.3">خبرٌ يهزّ قلبك</div></div>

<div class="sc"><div class="e chip" data-a="9.6" data-b="14.6" style="font-size:36px">لم يُطلب منه أن يوقف الطوفان… بل أن يصنع</div>
 <div class="e ay" data-a="10.2" data-b="14.6">﴿فَأَوْحَيْنَا إِلَيْهِ أَنِ اصْنَعِ الْفُلْكَ بِأَعْيُنِنَا وَوَحْيِنَا﴾</div>
 <div class="e ref" data-a="10.8" data-b="14.6">[المؤمنون: من الآية ٢٧]</div></div>

<div class="sc"><div class="e mid" data-a="14.9" data-b="19.6">«اصنع»… جهدك<br>«بأعيننا»… رعاية الله</div>
 <div class="e mid g" data-a="16.4" data-b="19.6" style="margin-top:30px;font-size:58px">اليقين ليس أن تنتظر النجاة…<br>بل أن تبنيها وأنت مطمئن</div></div>

<div class="sc"><div class="e chip" data-a="19.9" data-b="25.4">📖 «هندسة اليقين»: رحلة في خمس سور</div>
 <div class="srs" style="gap:12px">
 <div class="e sr" data-a="20.2" data-b="25.4" style="padding:10px 36px"><b style="font-size:50px">المؤمنون</b><span>الإيمان</span></div>
 <div class="e sr" data-a="20.6" data-b="25.4" style="padding:10px 36px"><b style="font-size:50px">النور</b><span>البصيرة</span></div>
 <div class="e sr" data-a="21.0" data-b="25.4" style="padding:10px 36px"><b style="font-size:50px">الحجرات</b><span>العلاقات</span></div>
 <div class="e sr" data-a="21.4" data-b="25.4" style="padding:10px 36px"><b style="font-size:50px">العنكبوت</b><span>الثبات في البلاء</span></div>
 <div class="e sr" data-a="21.8" data-b="25.4" style="padding:10px 36px"><b style="font-size:50px">الحديد</b><span>الدنيا والمال</span></div></div>
 <div class="e mid g" data-a="22.6" data-b="25.4" style="margin-top:28px;font-size:56px">تبني في داخلك ما لا تهدمه العواصف</div></div>

<div class="sc"><div class="e big" data-a="25.7" data-b="29.6">أعطيتَ عملك<br>يومك كله…</div>
 <div class="e mid g" data-a="27.0" data-b="29.6" style="margin-top:26px">فامنح قلبك دقائق<br>تبني فيها لوحاً في سفينته 🤍</div></div>

<div class="sc" style="padding-top:150px"><img class="e cover" data-a="29.9" data-b="99" src="file:///home/claude/handasatalyaqeen/social/brand/book-cover.jpg" style="width:360px;margin:10px 0 34px">
 <div class="e big" data-a="30.1" data-b="99" style="font-size:78px">هندسة اليقين</div>
 <div class="e mid" data-a="30.4" data-b="99" style="margin-top:14px;font-size:50px">43 محطة تبني يقيناً يصمد</div>
 <div class="e big g" data-a="30.8" data-b="99" style="margin-top:46px;font-size:76px">🎁 اقرأ محطة كاملة ببلاش</div>
 <div class="e btn" data-a="31.2" data-b="99" style="margin-top:34px;font-size:46px;padding:24px 50px">راسلنا على واتساب ←</div></div>
'''
open('ad-jordan.html','w').write(head+B+'\n'+script)
