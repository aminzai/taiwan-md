---
title: "Đường Phượng: Mỗi quyết định nổi tiếng của cô đều là sự từ chối nhãn mác 'thiên tài'"
description: "Bị bạn học đá ngất lúc 8 tuổi, từ chối được tuyển thẳng vào trường Kiến Trung năm 14 tuổi, công khai xu hướng tính dục khi còn 24 tuổi nhưng từ chối làm đại sứ, và điều kiện đầu tiên khi gia nhập hội đồng ở tuổi 35 là 'không có văn phòng'. Vào ngày 2 tháng 12 năm 2025 tại Stockholm, cô nhận Giải thưởng Sinh kế Đúng đắn (Right Livelihood Award), trên sân khấu không nói về 'tôi' mà nói về 'chúng ta'."
date: 2026-05-16
category: 'People'
tags:
  [
    'nhân vật',
    'đường phượng',
    'bộ phát triển kỹ thuật số',
    'g0v',
    'khác giới',
    'lập trình',
    'chính phủ mở',
    'vTaiwan',
    'đa dạng',
    'giải thưởng sinh kế đúng đắn',
  ]
subcategory: '教育與社會'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-05-16
lastHumanReview: true
readingTime: 14
image: '/article-images/people/audrey-tang-portrait-2016.webp'
imageAlt: 'Ảnh chân dung Đường Phượng được chụp vào tháng 3 năm 2016 tại Paris, mặc trang phục tối màu, ánh sáng tự nhiên dịu nhẹ.'
imageCredit: 'Camille McOuat (Flickr / Wikimedia Commons, CC BY 2.0)'
lifeTree:
  protagonist: '唐鳳（Audrey Tang）'
  birthYear: 1981
  span: '1981–2025'
  source:
    article: 'knowledge/People/唐鳳.md'
    commit: 'pending'
    commitDate: '2026-05-16'
    extractedBy: 'Taiwan.md (Semiont) γ-evolve'
    extractedAt: '2026-05-16 +0800'
    note: '原文 references = 中文維基 / 臺灣女人 NMTH / 數位發展部官網 / Right Livelihood / 江明宗 Medium 等多源 cross-verify。多數重大轉折由本人公開談過，counterfactual 主要為結構性對比。'
  intro: '8 歲停學、14 歲拒絕保送建中、19 歲在矽谷當工程師、24 歲跨性別出櫃、35 歲成為全球首位跨性別部長。她每一次「離開主流軌道」都不是反叛而是選擇。這棵樹列出她選的路，也列出她沒選的——所有 alternative 都有同代結構性對照。'
  themes:
    - id: 'education'
      label: '體制 vs 自學'
      color: '#8B5CF6'
    - id: 'identity'
      label: '隱身 vs 出櫃'
      color: '#EC4899'
    - id: 'tech-policy'
      label: '純技術 vs 政治參與'
      color: '#10B981'
    - id: 'tools'
      label: '個人 vs 社群協作'
      color: '#F59E0B'
  nodes:
    - id: 'birth'
      year: 1981
      age: 0
      type: 'given'
      theme: 'education'
      label: '出生於台北（原名唐宗漢）'
      scene: '智商測驗校方做過 3 次都是「至少 160」最高等級。母親李雅卿是《中國時報》採訪組副主任，後來是教育改革者。'
    - id: 'drop-out-8'
      year: 1989
      age: 8
      type: 'choice'
      theme: 'education'
      scene: '9 年內轉換 3 所幼稚園、6 所小學；小二曾因搶考卷被同學踢一腳撞牆昏倒'
      chose:
        label: '正式停學在家自學'
        consequence: '母親洗澡時看見肚子瘀青，當下決定為她辦休學。後來李雅卿帶她到德國體驗另類教育，1994 年回台創辦烏來種籽親子實驗小學。'
      alternatives:
        - label: '繼續在體制內適應'
          plausibility: 'structural'
          note: '同代多數高智商但社交困難的孩子被診斷為亞斯/ADHD，繼續在體制內掙扎。如果留在學校，可能會走出版或學術路徑（亦可能更早 burnout）。'
        - label: '轉到資優教育班'
          plausibility: 'structural'
          note: '台灣 1980s 末已有資優教育班。如果走資優班，會跟其他高智商孩子一起被體制塑形，少了完全自由探索的時間。'
    - id: 'refuse-jianzhong'
      year: 1995
      age: 14
      type: 'choice'
      theme: 'education'
      scene: '獲得保送建中的資格'
      chose:
        label: '放棄建中 + 完全自學程式設計'
        consequence: '14 歲在烏來山中閉關後，向父母宣告不再升學。沒有老師、沒有課程，靠閱讀技術文件 + 網路社群學習。為日後推動開放教育與知識共享奠定理念基礎。'
      alternatives:
        - label: '念建中走台灣資優生路徑'
          plausibility: 'structural'
          note: '建中 → 台大 → 海外名校的標準路徑。如果走，會有正規學歷加持，但失去「14 歲就在 internet 上跟全球工程師對話」的塑形時期。'
        - label: '出國念中學'
          plausibility: 'structural'
          note: '同代部分天才兒童家庭選擇早期送出國（如 MIT 早期入學）。如果走，可能更早接觸世界一流計算機科學，但 g0v 那條公民科技線不會在台灣發生。'
    - id: 'silicon-valley'
      year: 2000
      age: 19
      type: 'choice'
      theme: 'tech-policy'
      scene: '19 歲已在加州矽谷軟體公司擔任工程師'
      chose:
        label: '深耕程式語言理論（Perl/Haskell）+ 發起 Pugs 專案'
        consequence: '2005/2/1 啟動 Pugs（用 Haskell 實現 Perl 6）。2001-2006 在 CPAN 啟動超過 100 個 Perl 專案。「用一種語言實現另一種語言」訓練了她的 meta-thinking——後來看政府就像看一個需要重構的系統。'
      alternatives:
        - label: '加入 Google / 大型科技公司'
          plausibility: 'structural'
          note: '2000 年代矽谷主流路徑。如果走，會有更高薪 + 股票，但失去 open source 社群浸淫時間。後來 g0v 的「不是員工是社群」DNA 不會出現。'
        - label: '創業'
          plausibility: 'structural'
          note: '同代矽谷工程師很多選擇創業（YC 第一批 2005）。如果走，可能成為連續創業者，但「為公共利益寫 code」的傾向會被「為股東寫 code」覆蓋。'
    - id: 'gender-transition'
      year: 2005
      age: 24
      type: 'choice'
      theme: 'identity'
      scene: '人生最重要的決定之一'
      chose:
        label: '服用雌激素 + 公開出櫃 + 改名「唐鳳」'
        consequence: '2005 年底在 blog.elixus.org 部落格自行宣告。「不管現在、過去或未來，我很樂意大家用女性的名詞來稱呼我」。父親回應「沒有理由不接受」。為台灣 LGBTQ+ 權益做出重要貢獻，但她本人後來反覆拒絕「跨性別代言人」位置，自稱「後類別」。'
      alternatives:
        - label: '私下轉換不公開'
          plausibility: 'structural'
          note: '部分跨性別者選擇低調 transition，避免社會壓力。如果走這條，職涯可能更平順，但「全球首位公開跨性別部長」的歷史地位不存在。'
        - label: '不 transition'
          plausibility: 'speculative'
          note: '[推測] 同代部分跨性別者因社會壓力選擇延後或放棄。如果走，內在張力可能影響後續創造力與公開能見度。'
    - id: 'g0v-2012'
      year: 2012
      age: 31
      type: 'choice'
      theme: 'tools'
      scene: '在矽谷已是有聲譽的開源工程師'
      chose:
        label: '與高嘉良、吳泰輝、瞿筱葳等共創 g0v 零時政府'
        consequence: "台灣最重要的公民科技社群。起點是 2012/10 對「經濟動能推升方案」廣告的不滿 + 中央政府總預算視覺化。「hack don't attack」——不攻擊既有制度，用技術改善它。萌典、IVOD、口罩地圖等模式後來被全球複製。"
      alternatives:
        - label: '繼續在矽谷做純技術'
          plausibility: 'structural'
          note: '當時矽谷對她已開放各種 senior 機會。如果留下，會是「另一個成功的台裔工程師」，不會有後來的政策影響力。'
        - label: '回台灣加入既有政黨/智庫'
          plausibility: 'structural'
          note: '走傳統政治參與路徑。如果走，會被政黨機器收編，「無黨籍政務委員」的可能性消失。'
    - id: 'sunflower'
      year: 2014
      age: 33
      type: 'choice'
      theme: 'tech-policy'
      scene: '2014/3/18 太陽花學運佔領立法院'
      chose:
        label: '一手架設場內所有線路、鏡頭、網路直播設備，但本人只待議場 1 小時即離開'
        consequence: '她認為「議場內部 5 個不同角度攝影機錄影和直接播出的情況下，所有活動已經成為純粹的展示演出和儀式」。對佔領、表態都「不感興趣」。同時自掏腰包請人做政府會議逐字稿。'
      alternatives:
        - label: '完全參與佔領 / 公開表態反政府'
          plausibility: 'structural'
          note: '同代部分技術人選擇成為運動代言人。如果走，可能成為政治明星，但失去 2016 以「無黨籍 outsider」入閣的可能性。'
    - id: 'vtaiwan'
      year: 2014
      age: 33
      type: 'choice'
      theme: 'tech-policy'
      scene: '2014/4 蔡玉玲以政務委員身份進到 g0v 黑客松，後續發展為 vTaiwan 平台'
      chose:
        label: '與政府合作 vTaiwan + Pol.is 共識引擎'
        consequence: '2015-2018 處理 26 議題，80% 引起實質政府行動。Uber 法規討論成最知名案例。國際公認的數位民主典範。'
      alternatives:
        - label: '拒絕與政府合作'
          plausibility: 'structural'
          note: '部分公民科技人堅持與政府保持距離（如 EFF 路線）。如果如此，g0v 純民間倡議路徑，不會被「招安」進體制，但也少了實際政策落地能力。'
    - id: 'digital-minister'
      year: 2016
      age: 35
      type: 'choice'
      theme: 'tech-policy'
      scene: '2016/8/9 第一次見林全、8/15 同意接任、10/1 上任'
      chose:
        label: '入閣擔任「數位政委」，談妥三條件：每週三、五遠距上班 / 會議全公開逐字稿 / 不必每天進院'
        consequence: '台灣史上最年輕政務委員 + 全球第一個公開跨性別身份的部長級政治人物 + 台灣第一位「數位政委」。'
      alternatives:
        - label: '婉拒入閣'
          plausibility: 'structural'
          note: '同類型的 outsider 技術人有人婉拒（怕被體制吸納）。如果婉拒，數位轉型工作會缺一個關鍵連結點，後來疫情口罩地圖等可能晚數月或不發生。'
    - id: 'covid-mask-map'
      year: 2020
      age: 39
      type: 'choice'
      theme: 'tools'
      scene: '2020/1/31 - 2/6 期間，吳展瑋凌晨用 Google Maps API 做的超商口罩地圖一夜燒掉 2 萬美元 API 費用'
      chose:
        label: '協調健保署 open data 釋出 + 邀集 g0v 社群共同開發藥局口罩採購地圖'
        consequence: '2/6 健保署 open data 上線同日，藥局口罩採購地圖正式上線。24 小時內 100 萬人次使用。2/15 HackMD 上有 101 個相關應用、g0v 社群建構 140+ 工具。江明宗 verbatim：「唐鳳有決定權，還能自己改 code，所以我們都不用北上向哪個長官報告」。'
      alternatives:
        - label: '只做政策不下海寫工具'
          plausibility: 'structural'
          note: '部會首長正常路徑：開會、定政策、讓承包商做。如果如此，口罩地圖可能變成 6 週才上線的官方 app（多國的 reality）。她下海推 g0v 社群跑兩天上線是關鍵。'
    - id: 'moda-minister'
      year: 2022
      month: 8
      age: 41
      type: 'choice'
      theme: 'tech-policy'
      scene: '2022/8/27 數位發展部正式揭牌'
      chose:
        label: '擔任首任部長至 2024/5/20'
        consequence: '從跨部會協調的政務委員變成有固定預算與編制的正式部長。整合電信、資安、數位經濟。首年預算員額 598 人、公務預算 57 億 + 前瞻 160 億。任期 1 年 9 個月。'
      alternatives:
        - label: '繼續當政務委員不擔任部長'
          plausibility: 'structural'
          note: '保留「跨部會自由」的彈性，避免成為被質詢的固定靶。但失去「正式部會 + 預算 + 編制」的執行力。'
        - label: '回民間繼續做 g0v'
          plausibility: 'structural'
          note: '另一條路：以 NGO 身份持續影響政策。如果走，數位發展部首任部長會是別人，很可能用更傳統官僚方式管理。'
    - id: 'stockholm'
      year: 2025
      month: 12
      age: 44
      type: 'choice'
      theme: 'tools'
      scene: '2025/12/2 斯德哥爾摩 Right Livelihood Award 頒獎台'
      chose:
        label: '接受「另一個諾貝爾獎」，台上演說將焦點推回集體'
        consequence: "首位獲此獎台灣人。Citation：「For advancing the social use of digital technology to empower citizens, renew democracy and heal divides」。接受演說 verbatim：「Cyberspace is a conflict region, and my work turns that conflict into an energy source for co-creation」+ 個人哲學重述「The superintelligence we are looking for is already here. It's us」。"
      alternatives:
        - label: '在頒獎台上講「我的成就」'
          plausibility: 'structural'
          note: '同代得獎者常以個人故事為敘事中心。如果走，獎座變成個人勳章，但她選擇把舞台 reframe 成「我們」——她拒絕當天才這條主線的最後一個變奏。'
translatedFrom: 'People/唐鳳.md'
sourceCommitSha: 'e75b621d2'
sourceContentHash: 'sha256:1917aa69dfd8ab97'
translatedAt: '2026-09-22T06:37:45.226921+00:00'
---

# Đường Phượng: Mỗi quyết định nổi tiếng của cô đều là sự từ chối nhãn mác "thiên tài"

> **Tóm tắt 30 giây:**
> Bị bạn học đá ngất và nghỉ học năm 8 tuổi, từ chối được tuyển thẳng vào trường Kiến Trung năm 14 tuổi, công khai xu hướng tính dục khi còn 24 tuổi nhưng từ chối làm đại sứ, điều kiện đầu tiên khi gia nhập nội các ở tuổi 35 là "không có văn phòng". Vào rạng sáng năm 2020, cô và Giang Minh Tông cùng viết mã để lập bản đồ khẩu trang trên Slack của g0v; vào ngày 2 tháng 12 năm 2025 tại Stockholm, khi nhận Giải thưởng Sinh kế Đúng đắn (Right Livelihood Award), trong khi mọi người đều mong đợi câu chuyện cá nhân của cô, điều cô nhấn mạnh trên sân khấu lại là từ "chúng ta". Thế giới coi cô là thiên tài; nhưng mỗi quyết định nổi tiếng của cô đều là sự từ chối vị trí đó.

## Bản đồ khẩu trang "đốt" hai vạn đô la

Cuối tháng 1 năm 2020, đại dịch COVID-19 bắt đầu lan rộng tại Đài Loan. Nguồn cung khẩu trang ở các hiệu thuốc trở nên khan hiếm, và chính phủ thông báo thực hiện mua hàng theo tên người vào ngày 6/2. Vào rạng sáng ngày 2 tháng 2, một kỹ sư tên Ngô Triển Vĩ (Howard) từ studio 好想 (Hao Xiang) đã tự mình tạo ra một bản đồ sử dụng Google Maps API để tra cứu lượng khẩu trang tại các cửa hàng tiện lợi lân cận. Anh ấy triển khai và chia sẻ nó trên mạng xã hội vào rạng sáng[^1].

Buổi trưa, sau khi ăn xong, anh quay lại máy tính thì thấy hóa đơn phía sau của Google API đã lên tới 20.000 đô la Mỹ—số lượng sử dụng trong vòng 24 giờ đã "đốt" hết số tiền này.

Ngày hôm đó, Đường Phượng xuất hiện trên kênh Slack của g0v. Cô không đến để ra lệnh. Cô phối hợp với đội ngũ kỹ sư Google để kiềm chế hóa đơn tại thời điểm đó; đồng thời cùng một vài người bạn lâu năm trong cộng đồng g0v—Giang Minh Tông (kiang, thư ký trước của Văn phòng Thành phố Thông minh Đài Nam), các thành viên nhóm thông tin của Cơ quan Bảo hiểm Y tế Quốc gia (Trương Linh Chi, Trần Tư Du)—cùng nhau suy nghĩ: làm thế nào để lượng khẩu trang tại hơn 6.000 hiệu thuốc trên toàn Đài Loan được đồng bộ hóa mỗi 30 giây lên một bản đồ mà bất kỳ ai cũng có thể truy cập[^2]?

Vào lúc 8 giờ sáng ngày 6/2, bản đồ mua sắm khẩu trang của Cơ quan Bảo hiểm Y tế Quốc gia đã chính thức được công bố thông qua dữ liệu mở. Trong 24 giờ, nó đã được hơn 1 triệu người sử dụng. Đến ngày 15/2, HackMD đã tích lũy được 101 ứng dụng liên quan, và cộng đồng g0v đã tạo ra hơn 140 công cụ[^2][^3].

Giang Minh Tông sau đó đã ghi lại đoạn này trong bản thảo bài phát biểu của mình:

> ✦ "Bí thư Đảng ủy rất thành thạo về kiến trúc thông tin, chúng tôi đưa ra bất kỳ yêu cầu nào cô ấy đều hiểu. Điều quan trọng nhất là Đường Phượng có quyền quyết định và còn tự sửa code được, nên chúng tôi không cần phải báo cáo lên cấp trên ở Bắc Kinh."[^4]

Nhân vật chính của câu chuyện này không chỉ là Đường Phượng. Đó là Giang Minh Tông, Ngô Triển Vĩ, các công chức từ nhóm thông tin của Cơ quan Bảo hiểm Y tế Quốc gia, hàng trăm kỹ sư trong cộng đồng g0v, và cả những đêm thức trắng sửa code tại văn phòng của Đường Phượng.

Nhưng sau năm 2020, tất cả các phương tiện truyền thông nước ngoài đều viết rằng nhân vật chính chỉ là cô ấy. BBC viết "Audrey Tang cứu Đài Loan bằng code", Wired viết "Hacker trở thành Bộ trưởng Kỹ thuật số của Đài Loan", và TIME xếp cô vào danh sách "nhà lãnh đạo toàn cầu chống dịch bệnh".

Trong mỗi cuộc phỏng vấn, cô đều đẩy công lao về phía người khác. Nhưng câu chuyện về một "bộ trưởng thiên tài cứu Đài Loan" đã bám lấy cô hơn bốn mươi năm, và không dễ dàng gỡ bỏ được.

## Bị bạn đá ngất năm 8 tuổi, từ chối học trường Kiến Trung năm 14

Vào ngày 18 tháng 4 năm 1981, Đường Phượng (Tang Feng) sinh ra tại Đài Bắc. Tên trước của cô là Đường Tông Hán. Cha cô, Đường Quang Hoa (Tang Guanghua), từng là phó tổng biên tập của 《Trung Quốc Thời Báo》; mẹ cô, Lý Nhã Khanh (Li Yaqing), là phó giám đốc bộ phận phỏng vấn của tờ báo này[^5].

Cô mắc bệnh tim bẩm sinh. Nhà trường đã thực hiện ba lần kiểm tra trí thông minh, mỗi lần đều cho kết quả "ít nhất 160" (mức cao nhất của công cụ kiểm tra). Khi cô 8 tuổi, nhà chưa có máy tính, nhưng cô đã đọc một cuốn sách lập trình Applesoft BASIC, và tự vẽ bàn phím cùng màn hình máy tính trên giấy, ghi lại các nút bấm và nội dung mà máy tính có thể xuất ra[^5].

Nhưng nhãn mác "thiên tài" có lẽ là tính từ được nhắc đến nhiều nhất bên cạnh tên cô vào năm 2026, chứ không phải ở đứa trẻ 8 tuổi năm 1989. Ở vị trí đó chỉ có những trận đánh đập, vết bầm tím và câu hỏi: "Tại sao con không chết đi?".

Lớp sáu tiểu học, cô đã chuyển ba nhà trẻ và sáu trường tiểu học. Một ngày nọ ở lớp hai, sau khi giáo viên phát bài kiểm tra và rời khỏi phòng học, Đường Phượng đã làm xong sớm. Vài bạn chưa viết được đã đưa tay đòi giật bài kiểm tra của cô. Cô chạy mang bài kiểm tra, bị ngã, và một bạn học sinh đã dốc hết sức đá vào cô, khiến cô đập vào tường và ngất xỉu[^6]. Sau đó, bạn học đó đã nói một câu mà tờ Kim Chuẩn ghi lại nguyên văn:

> ✦ "Tại sao con không chết đi? Nếu con chết, tôi sẽ là người giỏi nhất."[^6]

Cô về nhà nhưng không nói gì. Một ngày nọ, mẹ cô nhìn thấy vết bầm tím trên bụng cô khi bà đang tắm, và quyết định cho cô nghỉ học[^6].

Sau này, mẹ Lý Nhã Khanh đã sang Đức nghiên cứu giáo dục thay thế, và vào năm 1994, bà thành lập trường tiểu học thí nghiệm Tinh Tử Tương Tử (Seed Family Experimental School) ở Ô Lai, tự nhận làm hiệu trưởng đầu tiên[^7]. Năm 1995, Đường Phượng, khi 14 tuổi, sau một thời gian ẩn dật trên núi Ô Lai, đã thông báo với cha mẹ: cô sẽ không học tiếp nữa, từ bỏ việc được tuyển thẳng vào trường Kiến Trung[^8].

Đó không phải là lựa chọn "tôi quá thiên tài nên không cần đến trường". Đó là quyết định của một đứa trẻ đã học cách tự giấu mình từ năm tám tuổi, rằng ở tuổi mười bốn, cô không muốn bị đóng khung trong vị trí "học sinh ưu tú" mà người khác gán cho.

Sau này, cô đã nói rất nhiều lần: "Tôi không nghĩ thế giới hiện đại còn có khái niệm thiên tài. Trong thời đại Internet, thực ra ai cũng là IQ 180."[^9]

## Năm 24 cô đổi tên, nhưng từ chối làm đại sứ chuyển giới

Năm 12 tuổi, cô bắt đầu học Perl[^10]. Đến năm 19 tuổi (năm 2000), cô đã là kỹ sư tại một công ty phần mềm ở Thung lũng Silicon, California[^11].

Vào ngày 1 tháng 2 năm 2005, khi 24 tuổi, cô khởi xướng dự án Pugs—một trình biên dịch và thông dịch Perl 6 được viết bằng Haskell[^12]. Pugs là một dự án "bootstrap" trong cộng đồng Perl: một ngôn ngữ tự hiện thực hóa bằng một ngôn ngữ khác. Trong khoảng thời gian từ năm 2001 đến năm 2006, cô đã khởi xướng hơn 100 dự án Perl trên CPAN[^13]. Cộng đồng mã nguồn mở quốc tế gọi cô là Audrey hoặc au.

Cuối năm 2005, cô tự tuyên bố mình là người chuyển giới trên blog của mình tại blog.elixus.org[^14]. Cô sử dụng estrogen nhưng chưa phẫu thuật. Tên tiếng Trung được đổi thành "Đường Phượng", và tên tiếng Anh Autrijus được đổi thành Audrey.

Trong bài viết trên blog đó, cô đã viết:

> ✦ “Dù là hiện tại, quá khứ hay tương lai, tôi rất sẵn lòng để mọi người gọi tôi bằng danh từ nữ.”[^14]

Phản hồi của cha cô, Đường Quang Hoa, khi được phỏng vấn sau này đã được nhiều phương tiện truyền thông trích dẫn nguyên văn:

> ✦ “Nếu con gái cảm thấy sự thay đổi giới tính giúp nó hạnh phúc hơn, phát huy sức sáng tạo tốt hơn mà không làm tổn hại đến bất kỳ ai, thì không có lý do gì để từ chối.”[^15]

Cô đã từ chối vị trí "đại sứ chuyển giới". Năm 2020, cô ghi mục giới tính là "Không" trong hồ sơ nhân sự của nội các. Khi đó, cô giải thích với phóng viên[^16]:

> ✦ “Tôi là ‘hậu phân loại’. Trong cuộc tranh luận về giới tính, tôi không đứng về phe nào. Điều đó không có nghĩa là tôi cho rằng vấn đề này không quan trọng, mà là tôi cho rằng cuộc tranh luận không thể giải quyết được bất kỳ vấn đề nào.”[^16]

Trong một cuộc phỏng vấn với Marie Claire, cô đã để lại một câu khác được trích dẫn nhiều lần:

> ✦ “Nếu bạn có thể chung sống với sự bối rối, dần dần bạn sẽ nhận ra rằng nó không phải là vấn đề của bạn cũng không phải là vấn đề của xã hội, mà là khoảng trống ở giữa. Mọi thứ đều có khoảng trống, và khoảng trống chính là lối vào ánh sáng.”[^17]

Từ năm 2010 đến 2016, cô kiêm nhiệm cố vấn cho Apple, tham gia phát triển Siri, với mức lương mỗi giờ được cho là tương đương một Bitcoin[^18]. Năm 33 tuổi (năm 2014), cô đã bàn giao công việc của Socialtext và Apple, tuyên bố "nghỉ hưu"[^11].

## g0v và Nghị trường Hoa Tai: Gán công lao cho những người vô hình

Vào tháng 10 năm 2012, bà cùng Cao Gia Lương (clkao), Ngô Thái Huy (Kirby), Qu Siêu Uy (ipa) và những người khác đồng sáng lập g0v Zero-Hour Government. Điểm khởi đầu là sự bất mãn với quảng cáo "Kế hoạch thúc đẩy động lực kinh tế" của chính phủ trung ương—một đoạn quảng cáo truyền thông có ngân sách 33 triệu, xem xong không biết chính phủ thực sự muốn làm gì[^19].

Dự án đầu tiên của g0v là trực quan hóa ngân sách nhà nước: biến các tài liệu ngân sách dày cộp thành những biểu đồ có thể nhấp chuột[^19]. Sau đó là MoeDict, IVOD (Phim trường Quốc hội), và việc phát sóng trực tiếp nghị trường trong cuộc vận động Hoa Tai.

Vào đêm ngày 18 tháng 3 năm 2014, sinh viên đã chiếm giữ nghị trường. Tất cả các đường truyền, camera và thiết bị phát trực tuyến trên mạng tại hiện trường đều do Đường Phượng tự dựng[^20].

Nhưng bà chỉ ở lại nghị trường một giờ rồi rời đi. Sau đó, PNN (Truyền hình Công cộng) đã phỏng vấn bà, và bà nói:

> ✦ "Với việc ghi hình và phát trực tiếp từ 5 góc độ khác nhau bên trong nghị trường, mọi hoạt động đều trở thành một màn trình diễn và nghi thức thuần túy."[^20]

Bà "không quan tâm" đến việc chiếm giữ hay tuyên bố. Điều bà quan tâm là công nghệ công cụ. Đồng thời, bà đã tự bỏ tiền thuê người ghi lại biên bản cuộc họp chính phủ—để những người không có mặt tại hiện trường cũng có thể đọc được toàn bộ cuộc đối thoại[^20].

Sau khi Hoa Tai kết thúc, vào tháng 4 năm 2014, Thái Ngọc Linh (Cai Yuling), một ủy viên chính sách lúc bấy giờ, đã tham gia hackathon của g0v. Kể từ thời điểm đó, hai khái niệm vốn đối lập là "chính phủ" và "g0v" bắt đầu nảy sinh một vùng giao thoa[^21].

Vùng giao thoa đó được gọi là vTaiwan. Từ năm 2015 đến 2018, nền tảng này đã xử lý 26 vấn đề, trong đó 80% đã dẫn đến hành động thực tế của chính phủ[^22]. Ví dụ nổi tiếng nhất là cuộc thảo luận về quy định Uber: các chủ xe taxi và những người ủng hộ Uber đã bế tắc sáu năm, cuối cùng đã hợp pháp hóa Uber với bảy điều kiện[^22].

Cốt lõi của nền tảng này là công cụ đồng thuận Pol.is—lượng lớn ý kiến được máy móc sắp xếp thành một số cụm (cluster), giúp mỗi người tham gia nhìn thấy "tôi giống ai, khác ai, và những luận điểm nào mà mọi người đều đồng ý". Nó không bỏ phiếu, không đối lập, mà chỉ vẽ ra hình dạng của sự bất đồng.

## Không văn phòng, bản ghi chép công khai toàn bộ, làm việc từ xa ba ngày mỗi tuần

Vào ngày 9 tháng 8 năm 2016, Đường Phượng (Audrey Tang) lần đầu tiên gặp Lâm Toàn (Lin Chuan), Thủ tướng Chính phủ. Vào ngày 15 tháng 8, bà đồng ý nhậm chức Ủy viên chính sách. Cuối tháng 9, bà trở về Đài Loan từ Thung lũng Silicon. Ngày 1 tháng 10, bà bắt đầu công tác tại Nội các[^23].

Ba điều kiện mà bà đã đàm phán trước sau này đã tạo ra một kẽ hở trong hệ thống công chức Đài Loan: làm việc từ xa vào thứ Tư và thứ Sáu hàng tuần; tất cả các cuộc họp đều có bản ghi chép công khai; không cần phải đến cơ quan mỗi ngày[^23].

Lâm Toàn đã giải thích với phóng viên lúc đó:

> ✦ "Hiện tại Nội các chưa có quy định về làm việc từ xa, nhưng mô hình làm việc lâu dài trước đây của bà ấy là làm việc từ xa. Tôi cho rằng, miễn là công việc không bị ảnh hưởng, việc truyền đạt ý tưởng hoặc chỉ thị chính sách qua máy tính từ xa là khả thi."[^24]

Bà đã trở thành ba điều: Ủy viên chính sách trẻ nhất trong lịch sử Đài Loan, nhân vật cấp bộ đầu tiên trên thế giới công khai về bản dạng giới xuyên giới, và "Ủy viên chính sách kỹ thuật số" đầu tiên của Đài Loan[^25].

Bà không có văn phòng cố định tại Nội các. Bà nói toàn bộ khu vực cơ quan là không gian làm việc của bà. Sau khi cuộc họp kết thúc, bản ghi chép được đăng tải trên sayit.pdis.nat.gov.tw, và bất kỳ ai cũng có thể tìm kiếm[^26].

Bà đã thành lập một nhóm nhỏ gồm 20 người, gọi là PDIS (Public Digital Innovation Space - Không gian Đổi mới Kỹ thuật số Công cộng). Một nửa là các chuyên gia tư nhân, một nửa là lực lượng tình nguyện viên từ các bộ ngành. Trong kỳ nghỉ hè còn bổ sung thêm 30 thực tập sinh[^26]. Nó không phải là một tổ chức quan liêu—nó là một không gian làm việc.

Năm 2019, bà được bầu chọn vào danh sách "Top 100 Nhà Tư Tưởng Toàn Cầu" của tạp chí _Foreign Policy_ (dựa trên bình chọn độc giả)[^27]. Truyền thông mô tả bà là "bộ trưởng duy nhất công khai xuyên giới trên toàn cầu", hay "ngôi sao lập trình". Trong mỗi cuộc phỏng vấn, bà đều đẩy công lao về phía người khác—nhưng câu chuyện về "bộ trưởng thiên tài" dễ được truyền lại hơn những gì bà nói.

![Đường Phượng phát biểu tại hội nghị xã hội số re:publica ở Berlin năm 2019](/article-images/people/audrey-tang-re-publica-2019.webp)
_Tại sự kiện đối thoại "Digital Social Innovation" của re:publica ở Berlin ngày 8 tháng 5 năm 2019, Đường Phượng cùng Julia Kloiber trên sân khấu. Ảnh: Jan Michalko. [CC BY-SA 2.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg).\_

## Chủ nghĩa vô chính phủ bảo thủ: Từ chối mệnh lệnh, cũng từ chối bị mệnh lệnh

Đường Phượng tự xưng là một "chủ nghĩa vô chính phủ bảo thủ". Thoạt nghe có vẻ mâu thuẫn.

"Bảo thủ" (conservative) mang ý nghĩa giữ lại các thể chế hiện hành và đang hoạt động tốt; còn "vô chính" (anarchist) là phản đối sự tập trung quyền lực, từ chối sự cưỡng ép từ trên xuống. Những người kết hợp hai từ này thường có ý: tôi tin rằng có những giá trị trong hệ thống hiện tại, nhưng tôi không tin bất kỳ ai có đủ tư cách để dùng uy quyền ép buộc người khác chấp nhận nó.

Trong cuộc phỏng vấn với Rest of World, bà đã để lại một câu gần như là lời tuyên ngôn:

> ✦ "Bất kỳ sự cưỡng ép nào từ trên xuống, dù đến từ giới tư bản hay nhà nước, đều tệ như nhau."[^28]

Khi được hỏi về "vai trò của mình" trong cuộc phỏng vấn với nhà kinh tế học Tyler Cowen, bà đã trả lời:

> ✦ "Tôi làm việc _cùng_ chính phủ; tôi không làm việc _cho_ chính phủ."[^29]

Trong phần Hỏi & Đáp tại Hội nghị Khoa học Máy tính Quốc tế (ICFP) năm 2020, bà cũng đưa ra nhận định này:

> ✦ "Ở Đài Loan chúng tôi có một ý tưởng kỳ lạ rằng truy cập internet băng thông rộng là một quyền cơ bản của con người. Mọi người đều nên có băng thông rộng. Nếu bạn không có, đó là lỗi cá nhân của tôi."[^30]

Từ "quyền con người" bà sử dụng rất nặng, nhưng từ "trách nhiệm cá nhân" lại dùng rất nhẹ. Thái độ công chức mà bà muốn hướng tới được gọi là "nếu thiếu chỗ nào, tôi sẽ đi lấp vào".

Trong triết lý làm việc của mình có một nguyên tắc là _humor over rumor_ (hài hước thay cho tin đồn). Khi hệ thống CoFacts phát hiện thông tin sai lệch lan truyền (viral disinformation), nhóm bà đã tung ra một video hai phút hoặc hai hình ảnh (dưới 200 từ) trong vòng hai giờ để đáp trả tin giả bằng sự hài hước. Đây được gọi là nguyên tắc 2-2-2[^31].

"Vụ hỗn loạn giấy vệ sinh" vào tháng 2 năm 2020 là một ví dụ được truyền thông quốc tế nhắc đến nhiều nhất cùng thời điểm: tin đồn lan truyền rằng khẩu trang và giấy vệ sinh dùng chung một loại bột giấy, khiến người dân hoảng loạn tích trữ; chính phủ đã tung ra một hình ảnh kèm theo (bức ảnh "chúng tôi chỉ có một viên thẻ" của Thủ tướng lúc bấy giờ là Tô Trinh Xương) trong vài giờ, giải thích chuỗi cung ứng với nguồn nguyên liệu khác nhau, và tin đồn đã hạ nhiệt vào ngày đó[^31]. Bà đã trình bày vụ này như một ví dụ về _humor over rumor_ trong các buổi phỏng vấn quốc tế tại TED: tin đồn không bị đàn áp bằng luật pháp mà bị che lấp bởi một bức ảnh vừa hài hước hơn, lại chứa đựng sự thật.

Ngày 27 tháng 8 năm 2022, Bộ Phát triển Kỹ thuật số chính thức được thành lập và bà nhậm chức bộ trưởng đầu tiên[^32]. Ngân sách nhân sự năm đầu là 598 người, ngân sách công là 5,7 tỷ Đài tệ cộng thêm 16 tỷ từ quỹ Tiên tiến, tổng cộng là 21,7 tỷ[^33].

Trong nhiệm kỳ của mình, bà đã thúc đẩy khả năng phục hồi kỹ thuật số (thuyết phục OneWeb của Anh và SES Luxembourg triển khai thiết bị đầu cuối tại Đài Loan), sửa đổi Luật Chữ ký điện tử đã hai mươi năm không được xem xét lại, đưa vào sử dụng nền tảng tin nhắn ngắn chuyên biệt cho chính phủ để chống lừa đảo, và yêu cầu 47 cơ quan cấp A áp dụng tiêu chuẩn truyền tải thống nhất T-Road trong vòng hai năm[^34][^35].

Nhưng bà cũng nhận nhiều lời chỉ trích mang tính xây dựng. Ông Kha Văn Triết của Đảng Dân gian đã chất vấn: "Trung bình mỗi người chi 30 triệu, đây là công việc gì?"; Nghị sĩ Lưu Thế Phương của Đảng Dân Tiến nói rằng "Bộ Phát triển Kỹ thuật số vẫn chưa tìm ra phương hướng"; và Nghị sĩ Ngô Nghiễm trong Đảng Quốc dân nhận xét: "Việc lừa đảo qua mạng mà người dân quan tâm nhất lại không có hành động thực chất"[^36][^37].

Ngay cả các công chức PO (Cán bộ Liên lạc Tham gia Công chúng) được bổ nhiệm vào các bộ ngành của PDIS cũng cảm thấy bối rối. Một phóng viên đã phỏng vấn một PO và ghi nhận lời này:

> ✦ "Tôi làm PO được hai tháng rồi, tôi cảm thấy nó là thêm một công việc, hiện tại vẫn chưa rõ rốt cuộc chúng ta có thể can thiệp bao nhiêu, có được cấp phép bao nhiêu... Tôi không biết vai trò của chúng ta trong các nền tảng này sau này sẽ là gì?"[^38]

Bà không thể trả lời câu hỏi đó. Hoặc nói đúng hơn, câu trả lời của bà là: tự bạn quyết định đi.

Cái giá phải trả cho việc "minh họa thay vì mệnh lệnh" là sự chậm chạp, là các chỉ số KPI không đẹp, và là hai năm mà vẫn chưa có ai có thể nói rõ ràng "Bộ Phát triển Kỹ thuật số đã làm gì". Bà đặt cược vào sự chuyển đổi văn hóa, và sự chuyển đổi văn hóa hoặc thành công hoặc thất bại.

Nhưng hệ thống SayIt ghi lại bản ghi âm công khai của PDIS đã tích lũy hơn 7000 cuộc họp cho đến ngày bà rời nhiệm sở[^26]. Bất kỳ ai nhập từ khóa "Uber", "khẩu trang", "LINE Pay" đều có thể đọc được từng lời bà đã nói với các nhà cung cấp, công chức và nghị sĩ vào thời điểm đó. Hệ thống này không tồn tại trước khi bà vào chính phủ, và cũng không ai gỡ bỏ sau khi bà rời đi. Bà không thể tóm gọn bằng một câu thành tích chính trị, nhưng bà thực sự để lại một hồ sơ đối thoại của chính phủ có thể tìm kiếm được trong bảy năm—điều này là lần đầu tiên trong lịch sử chính trị Đài Loan.

## Bục trao giải tại Stockholm, cô nói "chúng ta"

Vào tối ngày 20 tháng 5 năm 2024, sau lễ nhậm chức của Tổng thống Lại Thanh Đức, Đường Phượng đã vội vã đến Sân bay Cao Hùng. Trong ba tháng tiếp theo, bà đã đặt chân đến 20 quốc gia[^39].

Vào tháng 4 cùng năm, bà đã cùng nhà kinh tế học Glen Weyl và Cộng đồng Plurality phân tán toàn cầu xuất bản cuốn 《Plurality: The Future of Collaborative Technology and Democracy》. Cuốn sách này được phát hành dưới giấy phép CC0—nghĩa là bất kỳ ai cũng có thể làm bất cứ điều gì với toàn bộ nội dung của nó mà không cần ghi công, không cần trả phí và không cần xin phép[^40].

Trong cuốn sách mang tên "Plurality", họ sử dụng một ký tự Hán tự: ⿻ (phiên âm tiếng Trung là _zhòng_). Ký tự này thuộc loại "ký tự mô tả ý nghĩa" trong Unicode, được dùng để mô tả cấu trúc "hai thứ đan xen vào nhau". Bà giải thích với truyền thông quốc tế rằng ⿻ nhấn mạnh sự "đan xen" (_interweaving_)—sự khác biệt của nhiều cá thể không bị xóa bỏ, mà tạo thành một kết cấu tổng thể. Khái niệm này hoàn toàn trái ngược với "thiên tài": thiên tài là một điểm sáng được bao quanh bởi màu xám; còn ⿻ là mỗi sợi chỉ đều được các sợi khác quấn vào và không thể thiếu.

Vụ việc vTaiwan xử lý quy định của Uber thường được bà dùng để minh họa cho ⿻: Các chủ xe taxi và những người ủng hộ Uber đã bế tắc suốt sáu năm, cuối cùng đã hợp pháp hóa Uber với bảy điều kiện bổ sung[^22]. Sự đồng thuận này không có bên nào hoàn toàn "thắng", nhưng cũng không có bên nào hoàn toàn "thua". Bà nói đó mới là hình thái thực sự của nền dân chủ—là công việc dệt kết cấu của tất cả mọi người vào cùng một tấm vải.

Vào ngày 7 tháng 10, Bộ Ngoại giao bổ nhiệm bà làm Đại sứ Không kiêm nhiệm Trung Hoa Dân Quốc (Cyber Ambassador-at-Large)[^41]. Trên trang cá nhân audreyt.org và cyberambassador.tw của bà, câu mở đầu không thay đổi là:

> ✦ "Tôi muốn trở thành một vị tổ tiên đủ tốt cho các thế hệ tương lai."[^42]

Ngày 2 tháng 12 năm 2025, tại phòng trao giải của Quỹ Right Livelihood ở Stockholm. Giải thưởng Right Livelihood được gọi là "Giải Nobel thay thế" (Alternative Nobel Prize), được nhà từ thiện người Đức gốc Thụy Điển Jakob von Uexküll sáng lập vào năm 1980 nhằm bổ sung những lĩnh vực mà giải Nobel chưa bao quát.

Đường Phượng là người Đài Loan đầu tiên nhận giải này[^43]. Trích dẫn ghi như sau:

> ✦ "Vì đã thúc đẩy ứng dụng xã hội của công nghệ kỹ thuật số để trao quyền cho công dân, đổi mới nền dân chủ và hàn gắn sự chia rẽ."[^43]

Trong bài phát biểu nhận giải, điều đầu tiên bà nói không phải là những gì mình đã làm. Bà nói về không gian mạng (_cyberspace_):

> ✦ "Không gian mạng là một khu vực xung đột, và công việc của tôi biến xung đột đó thành nguồn năng lượng cho sự đồng sáng tạo. Đã đến lúc chúng ta thực hiện hòa bình trong khu vực này."[^43]

Sau đó bà nhắc lại câu trên trang bìa cuốn Plurality:

> ✦ "Siêu trí tuệ mà chúng ta đang tìm kiếm đã ở đây rồi. Đó chính là chúng ta."[^44]

Bà nhận giải thưởng được gọi là "Giải Nobel thay thế", sau đó chuyển trọng tâm sang "chúng ta"—người mà cả thế giới coi là thiên tài Đài Loan, một lần nữa từ chối vị trí "thiên tài".

Từ đứa trẻ 8 tuổi bị đá trong lớp học năng khiếu năm 1989, đến người phụ nữ 44 tuổi trên bục trao giải ở Stockholm năm 2025, đó là một con đường dài được lát bằng vô số những lời từ chối. Mỗi sự từ chối dường như là một hành động nổi loạn, nhưng nhìn lại tổng thể, chúng đều là các biến tấu của cùng một hành động: từ chối bị định nghĩa bởi vị trí "cá nhân xuất sắc", và tự đặt mình vào vai trò người xây dựng nút giao, cây cầu, không gian.

Bà từ chối làm thiên tài. Thế giới vẫn khăng khăng coi bà là thiên tài. Nhưng bà chưa bao giờ để thế giới chiến thắng cuộc tranh luận này—chỉ là thế giới cần rất nhiều thời gian mới hiểu được bà thực sự đang nói gì.

![Đường Phượng ký tên công khai năm 2021](/article-images/people/audrey-tang-signature.svg)
_Chữ ký cá nhân của Đường Phượng được công bố vào tháng 8 năm 2021, ban đầu dùng cho tạp chí Nhật Bản 《Văn Nghệ Xuân Thu》. Tác giả: bản thân Đường Phượng, [Miền công cộng CC0](https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg).\_

## Đọc thêm

- [Sodagreen: Từ sân khấu nhỏ ở Cống Liêu đến cuộc đấu tranh "Cá Tinh Mịch", một cuộc chiến giành lại chủ quyền âm nhạc kéo dài hai mươi năm](/vi/music/sodagreen) — Cũng là những cá thể khác biệt nổi lên trong thập niên 2000 của Đài Loan, cũng là sự phản kháng lâu dài nhằm "từ chối bị đóng khung bởi danh tính đã định", chỉ khác ở bối cảnh ngành công nghiệp âm nhạc chứ không phải chính phủ
- [Tiêu Thượng Nông](/vi/people/tony-hsiao-inside-founder) — Đồng sáng lập INSIDE và Ai Liệu Lợi, cũng tự định nghĩa vai trò của mình trong giới công nghệ Đài Loan bằng việc "vượt qua nhiều lĩnh vực"
- [Ngô Đại Du](/vi/people/tai-yu-wu) — Sự kế thừa các tinh hoa tri thức Đài Loan từ khoa học đến công nghệ; Ngô Đại Du với tư cách là Viện trưởng Viện Khoa học Trung Hoa đã đặt nền móng cho hệ thống nghiên cứu khoa học của Đài Loan
- [Quỹ Văn hóa Mở](/vi/technology/open-culture-foundation) — Một pháp nhân được thành lập từ người quản lý hậu trường g0v, trở thành cầu nối về nhân quyền số của Đài Loan; nhiều lần tương tác với Bộ Phát triển Số do Đường Phượng lãnh đạo, vừa hợp tác vừa giám sát
- [Đại dịch và vắc xin ở Đài Loan](/vi/society/taiwan-covid-pandemic-and-vaccines) — Chuỗi điều phối bản đồ khẩu trang đã tồn tại trong bối cảnh đại dịch như thế nào, và mười tám tháng mà Đài Loan nhận được nhờ biên giới và việc mua khẩu trang

## Nguồn hình ảnh

Bài viết này sử dụng 3 hình ảnh, tất cả đều được lưu trữ trong `public/article-images/people/` để tránh việc liên kết nóng đến máy chủ nguồn. Ba hình ảnh này có giấy phép CC / CC0 từ Wikimedia Commons:

- **hero**: [Chân dung Đường Phượng (cắt nhỏ)](<https://commons.wikimedia.org/wiki/File:Portrait_Audrey_Tang_(25915794061,_cropped).jpg>) — Ảnh: Camille McOuat, 09/03/2016 Paris, CC BY 2.0
- **scene-mid**: [Re:publica 19 - Ngày 3](<https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg>) — Ảnh: Jan Michalko, 08/05/2019 Berlin re:publica Hội nghị xã hội số hóa, CC BY-SA 2.0
- **signature**: [Chữ ký Đường Phượng](<https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg>) — Tác giả: Bản thân Đường Phượng, 18/08/2021, Miền công cộng CC0

## Tài liệu tham khảo

[^1]: [TechNews: Xây dựng bản đồ khẩu trang và tiết lộ đội ngũ đằng sau 'cứu quốc bằng bàn phím' (23/02/2020)](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — Trình bày chi tiết dòng thời gian của Ngô Triển Vĩ Howard với hóa đơn API 20.000 USD sau khi triển khai vào rạng sáng, và sự điều phối của Đường Phượng với Google và g0v

[^2]: [Medium của Giang Minh Tông: Bản đồ mua khẩu trang tại hiệu thuốc được ra mắt (Tháng 02/2020)](https://medium.com/%E6%B1%9F%E6%98%8E%E5%AE%97-kiang/%E8%97%A5%E5%B1%80%E5%8F%A3%E7%BD%A9%E6%8E%A1%E8%B3%BC%E5%9C%B0%E5%9C%96%E4%B8%8A%E7%B7%9A-54e11bd63e84) — Bản thân kỹ sư mô tả, nguyên văn 'Dữ liệu chính thức dự kiến sẽ lên vào lúc 8 giờ sáng ngày 6/2' + Đường Phượng điều phối sự tham gia của cộng đồng

[^3]: [Trang quyết định phòng chống COVID-19 của Bộ Y tế](https://covid19.mohw.gov.tw/ch/cp-4822-53563-205.html) — Mô tả chính thức của chính phủ, nguyên văn: 'Ủy viên phụ trách Đường Phượng của Viện Hành pháp mời các cộng đồng dân sự thông qua dữ liệu open data của Cơ quan Bảo hiểm Y tế để tạo ra nền tảng tra cứu khẩu trang phòng dịch'

[^4]: [TechNews: Xây dựng bản đồ khẩu trang (cùng [^1])](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — Xem thêm tài liệu trong liên kết gốc

[^5]: [Bài viết về Đường Phượng trên Wikipedia tiếng Trung](https://zh.wikipedia.org/zh-tw/%E5%94%90%E9%B3%B3) — Dữ liệu tiểu sử cơ bản về xuất thân / bối cảnh gia đình / tự học thời thơ ấu như bàn phím giấy BASIC

[^6]: [Tạp chí Kim Chuẩn: Bạn cùng lớp bị ghen ghét đánh ngất... Đường Phượng thiên tài từng có ý định tự sát nhiều lần khi còn nhỏ (11/2020)](https://www.businesstoday.com.tw/article/category/183035/post/202011090020/) — Cảnh đánh nhau trong lớp tiểu học + lời trích dẫn của bạn học 'Tại sao cô không chết đi' nguyên văn + quyết định nghỉ học sau khi mẹ phát hiện vết bầm khi tắm

[^7]: [Thời báo Trung Thị: Lý Nhã Khanh, phụ tá trẻ nhất của Đường Phượng, thực hành mô hình tự học cải cách giáo dục (25/08/2016)](https://www.chinatimes.com/realtimenews/20160825005980-260405) — Lý Nhã Khanh trở về Đài Loan năm 1992, sáng lập Trường Tiểu học Thí nghiệm Tự thân U Lai và làm hiệu trưởng đầu tiên vào năm 1994

[^8]: [Thai Báo: Thoát khỏi 'bắt nạt ở trường' để đi theo con đường tự học! Phát hiện 'quan trọng' của Đường Phượng khi 14 tuổi](https://www.taisounds.com/specialtopic/content/46/23226) — Sau khi nhốt mình ở U Lai năm 14 tuổi, cô từ chối được tuyển thẳng vào trường Jianzhong

[^9]: Nhiều phương tiện truyền thông trích dẫn, bản thân đã kể lại trong các cuộc phỏng vấn khác nhau: 'Tôi không nghĩ thế giới hiện đại còn có khái niệm thiên tài', 'Trong thời đại Internet, thực ra ai cũng là IQ 180'

[^10]: [Wikipedia: Audrey Tang](https://en.wikipedia.org/wiki/Audrey_Tang) — "Tang bắt đầu lập trình ở tuổi tám và bắt đầu học Perl ở tuổi 12"

[^11]: Bài viết về Đường Phượng trên Wikipedia tiếng Trung (cùng [^5]) — Năm 19 tuổi năm 2000 đã làm kỹ sư tại Thung lũng Silicon, và tuyên bố nghỉ hưu ở tuổi 33 vào năm 2014 sau khi chuyển giao Socialtext + Apple

[^12]: [Wikipedia: Pugs (trình biên dịch)](https://en.wikipedia.org/wiki/Pugs_(compiler) — Bài viết trên Wikipedia

[^13]: [Wikipedia: Audrey Tang (tiếng Anh)](https://en.wikipedia.org/wiki/Audrey_Tang) — "Tang đã khởi xướng hơn 100 dự án Perl từ tháng 6 năm 2001 đến tháng 7 năm 2006, bao gồm trình lưu trữ PAR nổi tiếng"

[^14]: Bài viết về Đường Phượng trên Wikipedia tiếng Trung (cùng [^5]) + nhiều phương tiện truyền thông trích dẫn nhất quán: 'Bất kể là hiện tại, quá khứ hay tương lai, tôi rất sẵn lòng để mọi người gọi tôi bằng danh từ giống cái'. Nguồn gốc là blog.elixus.org năm 2005

[^15]: [Tạp chí Kim Chuẩn: Phỏng vấn cha của Đường Phượng (Tháng 09/2016)](https://www.businesstoday.com.tw/article/category/80407/post/201609010032/) — Cha Đường Quang Hoa nguyên văn 'Không có lý do gì để không chấp nhận'

[^16]: [Nữ giới Đài Loan NMTH: Đường Phượng, thành viên nội các xuyên giới tính đầu tiên và cố vấn chính trị kỹ thuật số đầu tiên](https://women.nmth.gov.tw/?p=20105) — Đường Phượng verbatim nói rằng "Tôi là 'hậu loại'" + mục giới tính trong hồ sơ nhân sự nội các năm 2020 được điền là "Không"

[^17]: [Marie Claire Đài Loan: Đường Phượng kể về việc đối phó với sự bối rối sau khi bị bắt nạt thời thơ ấu](https://www.marieclaire.com.tw/entertainment/story/52923/audrey-tang) — verbatim "Mọi thứ đều có thiếu sót, và thiếu sót chính là lối vào của ánh sáng"

[^18]: [Bài viết Wikipedia tiếng Trung về Đường Phượng (cùng [^5])+](https://www.britannica.com/biography/Audrey-Tang) — Xem thêm tài liệu trong liên kết gốc

[^19]: [Tạp chí Quang Hoa Đài Loan: Công dân hacker g0v, chính phủ không thời gian](https://www.taiwan-panorama.com/Articles/Details?Guid=61281c3d-f79c-4db7-93d9-d18b29f90ba0) — Khởi điểm từ 2012/10 + trực quan hóa ngân sách tổng thể của chính phủ trung ương + danh sách đồng sáng lập

[^20]: [PNN Đài Truyền Hình Công Cộng: Báo cáo về phong trào Hoa Tai (2014)](https://news.pts.org.tw/article/327548) — verbatim "Tất cả các đường dây, máy quay, tất cả thiết bị phát trực tiếp trên mạng trong sự kiện đều do hacker công dân 'Đường Phượng' tự dựng lên" + bình luận của Đường Phượng về "buổi trình diễn và nghi thức" tại hội trường + tự trả tiền để ghi lại từng từ

[^21]: [Phóng viên: Tạo ra không gian đối thoại - Hành trình kỳ ảo của Đường Phượng](https://www.twreporter.org/a/g0v-audrey-tang) — verbatim sự tham gia của Thái Ngọc Linh vào hackathon g0v năm 4/2014 + nguồn gốc của vTaiwan

[^22]: [Democracy Technologies: Xây dựng đồng thuận ở Đài Loan](https://democracy-technologies.org/participation/consensus-building-in-taiwan/) — vTaiwan xử lý 26 vấn đề từ 2015-2018 / 80% dẫn đến hành động thực chất của chính phủ / hợp pháp hóa 7 điều kiện của Uber

[^23]: [Liberty Times: Phá vỡ truyền thống, Đường Phượng 'làm việc từ xa' vào thứ Tư và thứ Sáu hàng tuần (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859132) — Lần gặp Lâm Toàn đầu tiên vào 8/9 / Đồng ý vào 8/15 / Nhậm chức vào 1/10 / Ba điều kiện để gia nhập nội các

[^24]: [Liberty Times: Đường Phượng làm việc từ xa, Lâm Toàn: Điều này là khả thi (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859246) — Lâm Toàn verbatim nói rằng "Hiện tại chính phủ không có quy định về làm việc từ xa... điều này là khả thi"

[^25]: Bài viết Wikipedia tiếng Trung về Đường Phượng (cùng [^5]) — Thứ trưởng trẻ nhất trong lịch sử Đài Loan với 35 tuổi + nhân vật chính trị cấp bộ xuyên giới tính công khai đầu tiên trên toàn cầu

[^26]: [pdis.nat.gov.tw Hồ sơ công việc và hệ thống bản ghi âm công khai SayIt](https://sayit.pdis.nat.gov.tw/) — Cấu trúc nhóm PDIS gồm 20 người + một nửa là dân sự + một nửa là quân tình nguyện của bộ ngành + 30 thực tập sinh

[^27]: [Taipei Times: Audrey Tang được vinh danh trong "Top 100 Nhà Tư Tưởng Toàn Cầu" (25/01/2019)](https://www.taipeitimes.com/News/front/archives/2019/01/25/2003708586) — Được chọn vào Top 100 nhà tư tưởng toàn cầu của Foreign Policy (dựa trên phiếu bầu độc giả)

[^28]: [Rest of World: Tầm nhìn "anarcho-bảo thủ" của Audrey Tang về tương lai Đài Loan (2020)](https://restofworld.org/2020/audrey-tang-the-conservative-anarchist/) — verbatim "Bất kỳ sự cưỡng ép nào từ trên xuống, dù là từ giới tư bản hay nhà nước, đều xấu như nhau"

[^29]: [Conversations with Tyler Tập 106: Audrey Tang](https://conversationswithtyler.com/episodes/audrey-tang/) — verbatim "Tôi đang làm việc với chính phủ; tôi không làm việc cho chính phủ"

[^30]: [Lindsey trên X: Trích dẫn trực tiếp ICFP 2020 Q&A](https://x.com/lindsey/status/1297886318114963456) — verbatim "Ở Đài Loan chúng ta có một ý tưởng kỳ lạ rằng truy cập internet băng thông rộng là quyền con người"

[^31]: [SwissInfo: Tự do ngôn luận: Hài hước hơn tin đồn](https://www.swissinfo.ch/eng/politics/freedom-of-expression-humour-over-rumour-lessons-from-taiwan-in-digital-democracy/46592080) — Xem thêm tài liệu trong liên kết gốc

[^32]: [Trang web chính thức của Bộ Phát triển Kỹ thuật số: Các bộ trưởng nhiệm kỳ trước](https://moda.gov.tw/aboutus/ministers-since-2022/1527) — Nhiệm kỳ của Đường Phượng từ ngày 27 tháng 8 năm 2022 đến ngày 20 tháng 5 năm 2024 (nguyên văn)

[^33]: [Liberty Times: Đường Phượng sẽ phụ trách Bộ Phát triển Kỹ thuật số với 598 nhân viên biên chế](https://news.ltn.com.tw/news/politics/breakingnews/4021987) — Báo cáo của Liberty Times

[^34]: [Liberty Finance: Từ vị trí Bộ trưởng IT thiên tài đến giảng viên tự do - Tổng kết 3 thành tích và tranh cãi trong nhiệm kỳ Đường Phượng](https://ec.ltn.com.tw/article/breakingnews/4677986) — Khả năng phục hồi kỹ thuật số / OneWeb / Vệ tinh SES / Sửa đổi Luật Chữ ký điện tử / Nền tảng tin nhắn SMS mã ngắn 111

[^35]: [INSIDE: Một năm thành lập Bộ Phát triển Kỹ thuật số! Chi tiết hai thành tích và ba tranh cãi của Đường Phượng](https://www.inside.com.tw/article/32615-Taiwan-moda-anniversary) — Tiêu chuẩn truyền tải thống nhất T-Road của 47 cơ quan cấp A + Đồng nghiệp nói nguyên văn "So với các đơn vị trước đây, Đường Phượng sẵn lòng ủy quyền nhiều hơn"

[^36]: [Tạp chí Vision: Sau gần 1 năm 'Bộ Phát triển Kỹ thuật số' do Đường Phượng dẫn dắt được thành lập, giới bên ngoài chê không có thành tích](https://www.gvm.com.tw/article/105627) — Lời chỉ trích của Lưu Thế Phương / Ngô Nghiễm

[^37]: [ETtoday: Ngân sách 211 tỷ Đài tệ của Bộ Phát triển Kỹ thuật số, Kha Văn Triết ngạc nhiên: Trung bình mỗi người tiêu 30 triệu 'Đây là công việc gì?' (2022-08-30)](https://www.ettoday.net/news/20220830/2327863.htm) — Câu hỏi chất vấn của Kha Văn Triết

[^38]: [Phóng viên: Chính phủ mở, Đường Phượng đã vượt qua rào cản công chức như thế nào?](https://www.twreporter.org/a/open-government-audrey-political-commissar-challenges) — PO nói nguyên văn "Đã làm PO được 2 tháng... không rõ chúng ta có thể can thiệp bao nhiêu"

[^39]: [Liberty Finance: Từ vị trí Bộ trưởng IT thiên tài đến giảng viên tự do (cùng [^34])](https://ec.ltn.com.tw/article/breakingnews/4677986) — Báo cáo của Liberty Times

[^40]: [Plurality Institute: Ra mắt sách Plurality](https://www.plurality.institute/blog-posts/book-launch-plurality-the-future-of-collaborative-technology-and-democracy-by-e-glen-weyl-audrey-tang-and-the-plurality-community) — Đồng tác giả với Glen Weyl + Cộng đồng Plurality / Xuất bản ngày 16 tháng 4 năm 2024 / Phát hành CC0

[^41]: [Bài viết Wikipedia tiếng Trung về Đường Phượng (cùng [^5])+](https://cyberambassador.tw/) — Xem thêm tài liệu trong liên kết gốc

[^42]: [audreyt.org](https://audreyt.org/) — Xem thêm tài liệu trong liên kết gốc

[^43]: [Right Livelihood: Audrey Tang được trao Giải thưởng Sinh kế Đúng đắn (2025)](https://rightlivelihood.org/news/taiwans-audrey-tang-honoured-with-right-livelihood-award-for-advancing-digital-democracy-and-social-trust/) — Trích dẫn nguyên văn + Đoạn Đường Phượng phát biểu nguyên văn "Không gian mạng là một khu vực xung đột" + [Báo cáo của Focus Taiwan thông qua CCTV tiếng Anh](https://focustaiwan.tw/society/202512030022)

[^44]: cyberambassador.tw nguyên văn + Tái diễn giải triết học cuốn Plurality — "Trí tuệ siêu việt mà chúng ta tìm kiếm đã ở đây. Đó là chúng ta"
