<!--
  🤖 机器人 / VLM 主题深度定制版
  =====================================================
  配色：cyber green #00ff9c + 霓虹粉 #ff2d95 + 深空黑 #0a0e1a
  调性：自绘 SVG 机器人 + ROS2 节点架构图 + 终端风自我介绍
  =====================================================
-->

<div align="center">

<!-- 🤖 自绘机器人：脉冲天线 + 变色眼睛 + 旋转雷达 + 跳动信号条 -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="260" height="260">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0e1a"/>
      <stop offset="100%" stop-color="#1a1f3a"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop offset="0%" stop-color="#00ff9c" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#00ff9c" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <circle cx="160" cy="160" r="140" fill="url(#glow)"/>

  <!-- 头部 -->
  <rect x="70" y="80" width="180" height="140" rx="24" fill="url(#bg)" stroke="#00ff9c" stroke-width="3"/>

  <!-- 天线 + 脉冲球 -->
  <line x1="160" y1="80" x2="160" y2="42" stroke="#00ff9c" stroke-width="3"/>
  <circle cx="160" cy="34" r="7" fill="#ff2d95">
    <animate attributeName="opacity" values="1;0.25;1" dur="1.2s" repeatCount="indefinite"/>
    <animate attributeName="r" values="7;9;7" dur="1.2s" repeatCount="indefinite"/>
  </circle>

  <!-- 左眼 -->
  <circle cx="120" cy="135" r="20" fill="#0a0e1a" stroke="#00ff9c" stroke-width="2"/>
  <circle cx="120" cy="135" r="10" fill="#00ff9c">
    <animate attributeName="fill" values="#00ff9c;#ff2d95;#00ff9c" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="124" cy="131" r="3" fill="#ffffff"/>

  <!-- 右眼 -->
  <circle cx="200" cy="135" r="20" fill="#0a0e1a" stroke="#00ff9c" stroke-width="2"/>
  <circle cx="200" cy="135" r="10" fill="#00ff9c">
    <animate attributeName="fill" values="#00ff9c;#ff2d95;#00ff9c" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="204" cy="131" r="3" fill="#ffffff"/>

  <!-- 嘴（LED 信号强度条） -->
  <rect x="110" y="180" width="100" height="6" fill="#00ff9c"/>
  <rect x="110" y="190" width="80"  height="6" fill="#00ff9c" opacity="0.65"/>
  <rect x="110" y="200" width="50"  height="6" fill="#00ff9c" opacity="0.35"/>

  <!-- 雷达扫描环 -->
  <g transform="translate(275, 150)">
    <circle r="50" fill="none" stroke="#00ff9c" stroke-width="1" opacity="0.25"/>
    <circle r="35" fill="none" stroke="#00ff9c" stroke-width="1" opacity="0.5"/>
    <circle r="20" fill="none" stroke="#00ff9c" stroke-width="1" opacity="0.75"/>
    <line x1="0" y1="0" x2="50" y2="0" stroke="#ff2d95" stroke-width="2.5">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="2.5s" repeatCount="indefinite"/>
    </line>
    <circle r="3" fill="#ff2d95"/>
  </g>

  <!-- 底部跳动信号条 -->
  <g transform="translate(160, 240)">
    <rect x="-30" y="0" width="6" height="14" fill="#00ff9c"><animate attributeName="height" values="14;4;14"   dur="1.0s" repeatCount="indefinite"/></rect>
    <rect x="-18" y="0" width="6" height="10" fill="#00ff9c"><animate attributeName="height" values="10;18;10"  dur="1.2s" repeatCount="indefinite"/></rect>
    <rect x="-6"  y="0" width="6" height="20" fill="#00ff9c"><animate attributeName="height" values="20;6;20"   dur="0.8s" repeatCount="indefinite"/></rect>
    <rect x="6"   y="0" width="6" height="12" fill="#00ff9c"><animate attributeName="height" values="12;22;12"  dur="1.1s" repeatCount="indefinite"/></rect>
    <rect x="18"  y="0" width="6" height="16" fill="#00ff9c"><animate attributeName="height" values="16;8;16"   dur="0.9s" repeatCount="indefinite"/></rect>
  </g>
</svg>

# 🤖 Hi, I'm `asdasas1212`

<sub>👁️ Robotics · 🧠 VLM · 🧭 Navigation — building bots that <b>see, think, and move</b>.</sub>

```bash
$ whoami --robot
> asdasas1212 · Robotics & VLM enthusiast · 校招冲 Robotics / Embodied-AI

$ cat ./status.log
[●] Learning   : ROS2 + VLM 接入
[●] Building   : 视觉室内导航 demo
[●] Targeting  : 校招 Robotics / Embodied-AI 团队
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=700&color=00ff9c&center=true&vCenter=true&width=720&lines=Robotics+%2B+VLM+%2B+Navigation+%F0%9F%A4%96;%E6%9C%BA%E5%99%A8%E4%BA%BA%E8%A7%86%E8%A7%89%E5%AF%BC%E8%88%AA;See+the+world+%E2%9C%A8+Understand+the+world+%F0%9F%A4%96+Move+the+world;Let+the+robot+see+the+world%2C+and+be+seen" alt="Typing SVG" />

</div>

---

## 🧭 What I'm Building ｜ 我在做啥

<!-- ROS2 节点架构图：相机 → 感知 → 决策 → 底盘 -->
```mermaid
graph LR
  Cam[📷 RGB-D Camera] -->|Image|       CV[👁 OpenCV]
  Cam -->|PointCloud|                    PC[📐 PCL]
  CV  -->|Features|                      VLM[🧠 VLM<br/>Scene Graph]
  PC  -->|Map|                           SLAM[🗺 SLAM]
  VLM -->|Semantic|                      Nav[🧭 Nav2]
  SLAM -->|Pose|                         Nav
  Nav -->|cmd_vel|                       ROS[🤖 ROS2]
  ROS -->|Drive|                         Bot[🦾 Robot Base]

  style Cam  fill:#0a0e1a,stroke:#00ff9c,color:#00ff9c
  style CV   fill:#0a0e1a,stroke:#00ff9c,color:#00ff9c
  style PC   fill:#0a0e1a,stroke:#00ff9c,color:#00ff9c
  style VLM  fill:#1a1f3a,stroke:#ff2d95,color:#ff2d95
  style SLAM fill:#0a0e1a,stroke:#00ff9c,color:#00ff9c
  style Nav  fill:#1a1f3a,stroke:#ff2d95,color:#ff2d95
  style ROS  fill:#0a0e1a,stroke:#00ff9c,color:#00ff9c
  style Bot  fill:#1a1f3a,stroke:#ff2d95,color:#ff2d95
```

> 🔭 长期目标：把 VLM 当「机器人的大脑皮层」，让底盘听懂「去厨房拿个杯子」。

---

## 🛠 My Stack ｜ 工具链

<table>
<thead>
<tr>
<th align="center">👁️ 感知 Perception</th>
<th align="center">🧠 决策 Decision</th>
<th align="center">🦾 执行 Actuation</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top" width="33%">

- 📷 **OpenCV** — 图像处理 / 特征
- 🔥 **PyTorch** — 训练 / 推理
- 🎯 **YOLO** — 实时目标检测
- 📐 **PCL** — 点云处理
- ⚡ **CUDA** — GPU 加速

</td>
<td valign="top" width="33%">

- 🤖 **ROS2 Humble** — 节点通信
- 🐍 **Python** — 主力脚本
- ⚙️ **C++** — 性能关键路径
- 🧭 **Nav2** — 路径规划
- 🗺️ **SLAM** — 建图定位

</td>
<td valign="top" width="33%">

- 🐧 **Linux / Ubuntu** — 主力 OS
- 🐳 **Docker** — 环境隔离
- 📦 **CMake** — C++ 构建
- 🔧 **Git** — 版本控制
- 🐚 **Shell** — 自动化脚本

</td>
</tr>
</tbody>
</table>

---

## 📊 Live Stats ｜ 实时数据

<div align="center">

<!-- 🏆 奖杯墙 -->
<img src="https://github-profile-trophy.vercel.app/?username=asdasas1212&theme=radical&no-frame=true&margin-w=4&column=6" alt="Trophies" />

<br/>

<!-- 📈 总览 + 语言占比 -->
<img height="180em" src="https://github-readme-stats.vercel.app/api?username=asdasas1212&show_icons=true&count_private=true&include_all_commits=true&theme=radical&bg_color=0a0e1a&title_color=00ff9c&icon_color=00ff9c&text_color=ffffff&hide_border=true&border_radius=14" alt="GitHub Stats" />
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=asdasas1212&layout=compact&langs_count=8&theme=radical&bg_color=0a0e1a&title_color=00ff9c&text_color=ffffff&hide_border=true&border_radius=14" alt="Top Languages" />

<br/>

<!-- 🔥 连续打卡 + 👀 访客 -->
<img src="https://streak-stats.demolab.com/?user=asdasas1212&theme=radical&hide_border=true&background=0a0e1a&ring=00ff9c&fire=ff2d95&currStreakLabel=00ff9c" alt="GitHub Streak" />
<img src="https://komarev.com/ghpvc/?username=asdasas1212&color=00ff9c&style=flat" alt="Profile Views" />

<br/>

<!-- 🌐 3D 贡献图 -->
<img src="https://github-profile-3d-contrib.vercel.app/?username=asdasas1212&year=2025" alt="3D Contribution Graph" />

</div>

---

## 🐍 Contribution Snake ｜ 贪吃蛇

<!-- 启用方法：把 .github/workflows/snake.yml 复制进仓库 → Actions → Generate Snake → Run workflow -->

<div align="center">

  <img src="https://raw.githubusercontent.com/asdasas1212/asdasas1212/main/dist/github-contribution-grid-snake-dark.svg" alt="Snake Animation" />

</div>

---

<!-- 🌊 自绘扫描光带分隔线 -->
<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="6" viewBox="0 0 100 6" preserveAspectRatio="none">
  <defs>
    <linearGradient id="scan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#00ff9c" stop-opacity="0"/>
      <stop offset="50%"  stop-color="#00ff9c" stop-opacity="1"/>
      <stop offset="100%" stop-color="#ff2d95" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect y="1.5" width="100" height="3" fill="url(#scan)">
    <animate attributeName="x" values="-100;100" dur="3s" repeatCount="indefinite"/>
  </rect>
</svg>

<div align="center">

```bash
┌─[asdasas1212@github]─[~/readme]
└──╼ $ echo "robots > humans" && █
```

<sub>🤖 Let the robot see the world, and be seen by the world.</sub>

</div>
