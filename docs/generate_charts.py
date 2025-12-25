
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

warnings.filterwarnings('ignore')

# Set visualization style
plt.style.use('default')
sns.set_theme(style='whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

# ==========================================
# DATA LOADING
# ==========================================

# Manu Ginobili Career Data (Regular Season)
manu_seasons_rs = [
    {'Season': '2002-03', 'Team': 'SAS', 'G': 69, 'Min': 20.7, 'Pts': 7.6, 'Reb': 2.3, 'Ast': 2.0, 'Stl': 1.4, 'Blk': 0.2, 'TO': 1.4, 'FG%': .438, '3P%': .345, 'FT%': .737},
    {'Season': '2003-04', 'Team': 'SAS', 'G': 77, 'Min': 29.4, 'Pts': 12.8, 'Reb': 4.5, 'Ast': 3.8, 'Stl': 1.8, 'Blk': 0.2, 'TO': 2.1, 'FG%': .418, '3P%': .359, 'FT%': .800},
    {'Season': '2004-05', 'Team': 'SAS', 'G': 74, 'Min': 29.6, 'Pts': 16.0, 'Reb': 4.4, 'Ast': 3.9, 'Stl': 1.6, 'Blk': 0.4, 'TO': 2.3, 'FG%': .471, '3P%': .376, 'FT%': .803},
    {'Season': '2005-06', 'Team': 'SAS', 'G': 65, 'Min': 27.9, 'Pts': 15.1, 'Reb': 3.5, 'Ast': 3.6, 'Stl': 1.6, 'Blk': 0.4, 'TO': 1.9, 'FG%': .462, '3P%': .382, 'FT%': .770},
    {'Season': '2006-07', 'Team': 'SAS', 'G': 75, 'Min': 27.5, 'Pts': 16.5, 'Reb': 4.4, 'Ast': 3.5, 'Stl': 1.5, 'Blk': 0.4, 'TO': 2.1, 'FG%': .464, '3P%': .396, 'FT%': .860},
    {'Season': '2007-08', 'Team': 'SAS', 'G': 74, 'Min': 31.1, 'Pts': 19.5, 'Reb': 4.8, 'Ast': 4.5, 'Stl': 1.5, 'Blk': 0.4, 'TO': 2.7, 'FG%': .460, '3P%': .401, 'FT%': .860},
    {'Season': '2008-09', 'Team': 'SAS', 'G': 44, 'Min': 26.8, 'Pts': 15.5, 'Reb': 4.5, 'Ast': 3.6, 'Stl': 1.5, 'Blk': 0.4, 'TO': 2.0, 'FG%': .454, '3P%': .330, 'FT%': .880},
    {'Season': '2009-10', 'Team': 'SAS', 'G': 75, 'Min': 28.7, 'Pts': 16.5, 'Reb': 3.8, 'Ast': 4.9, 'Stl': 1.4, 'Blk': 0.3, 'TO': 2.1, 'FG%': .441, '3P%': .377, 'FT%': .800},
    {'Season': '2010-11', 'Team': 'SAS', 'G': 80, 'Min': 30.3, 'Pts': 17.4, 'Reb': 3.7, 'Ast': 4.9, 'Stl': 1.5, 'Blk': 0.4, 'TO': 2.2, 'FG%': .433, '3P%': .349, 'FT%': .871},
    {'Season': '2011-12', 'Team': 'SAS', 'G': 34, 'Min': 23.3, 'Pts': 12.9, 'Reb': 3.4, 'Ast': 4.4, 'Stl': 0.7, 'Blk': 0.4, 'TO': 1.9, 'FG%': .526, '3P%': .413, 'FT%': .800},
    {'Season': '2012-13', 'Team': 'SAS', 'G': 60, 'Min': 23.2, 'Pts': 11.8, 'Reb': 3.4, 'Ast': 4.6, 'Stl': 1.3, 'Blk': 0.2, 'TO': 2.2, 'FG%': .425, '3P%': .353, 'FT%': .700},
    {'Season': '2013-14', 'Team': 'SAS', 'G': 68, 'Min': 22.8, 'Pts': 12.3, 'Reb': 3.0, 'Ast': 4.3, 'Stl': 1.0, 'Blk': 0.3, 'TO': 2.0, 'FG%': .469, '3P%': .349, 'FT%': .850},
    {'Season': '2014-15', 'Team': 'SAS', 'G': 70, 'Min': 22.7, 'Pts': 10.5, 'Reb': 3.0, 'Ast': 4.2, 'Stl': 1.0, 'Blk': 0.3, 'TO': 2.2, 'FG%': .426, '3P%': .345, 'FT%': .721},
    {'Season': '2015-16', 'Team': 'SAS', 'G': 58, 'Min': 19.6, 'Pts': 9.6, 'Reb': 2.5, 'Ast': 3.1, 'Stl': 1.1, 'Blk': 0.2, 'TO': 1.7, 'FG%': .453, '3P%': .391, 'FT%': .810},
    {'Season': '2016-17', 'Team': 'SAS', 'G': 69, 'Min': 19.5, 'Pts': 7.5, 'Reb': 2.7, 'Ast': 2.7, 'Stl': 0.8, 'Blk': 0.2, 'TO': 1.3, 'FG%': .422, '3P%': .370, 'FT%': .907},
    {'Season': '2017-18', 'Team': 'SAS', 'G': 65, 'Min': 18.7, 'Pts': 9.0, 'Reb': 2.4, 'Ast': 2.3, 'Stl': 0.8, 'Blk': 0.2, 'TO': 1.3, 'FG%': .448, '3P%': .334, 'FT%': .827}
]

# Stephen Jackson Career Data (Regular Season)
jackson_seasons_rs = [
    {'Season': '2000-01', 'Team': 'NJN', 'G': 77, 'Min': 21.6, 'Pts': 8.2, 'Reb': 2.7, 'Ast': 1.8, 'Stl': 1.1, 'TO': 1.7, 'FG%': .425, '3P%': .335, 'FT%': .719},
    {'Season': '2001-02', 'Team': 'SAS', 'G': 23, 'Min': 9.9, 'Pts': 3.9, 'Reb': 1.1, 'Ast': 0.5, 'Stl': 0.7, 'Blk': 0.1, 'TO': 1.0, 'FG%': .374, '3P%': .250, 'FT%': .700},
    {'Season': '2002-03', 'Team': 'SAS', 'G': 80, 'Min': 28.2, 'Pts': 11.8, 'Reb': 3.6, 'Ast': 2.3, 'Stl': 1.6, 'Blk': 0.4, 'TO': 2.2, 'FG%': .435, '3P%': .320, 'FT%': .760},
    {'Season': '2003-04', 'Team': 'ATL', 'G': 80, 'Min': 36.8, 'Pts': 18.1, 'Reb': 4.6, 'Ast': 3.1, 'Stl': 1.8, 'Blk': 0.3, 'TO': 2.8, 'FG%': .425, '3P%': .340, 'FT%': .780},
    {'Season': '2004-05', 'Team': 'IND', 'G': 51, 'Min': 35.4, 'Pts': 18.7, 'Reb': 4.9, 'Ast': 2.3, 'Stl': 1.3, 'Blk': 0.3, 'TO': 2.4, 'FG%': .403, '3P%': .360, 'FT%': .830},
    {'Season': '2005-06', 'Team': 'IND', 'G': 81, 'Min': 35.9, 'Pts': 16.4, 'Reb': 3.9, 'Ast': 2.8, 'Stl': 1.3, 'Blk': 0.5, 'TO': 2.5, 'FG%': .411, '3P%': .345, 'FT%': .780},
    {'Season': '2006-07', 'Team': 'IND/GSW', 'G': 75, 'Min': 33.1, 'Pts': 15.5, 'Reb': 3.0, 'Ast': 3.8, 'Stl': 1.1, 'Blk': 0.5, 'TO': 2.4, 'FG%': .433, '3P%': .322, 'FT%': .810},
    {'Season': '2007-08', 'Team': 'GSW', 'G': 73, 'Min': 39.1, 'Pts': 20.1, 'Reb': 4.4, 'Ast': 4.1, 'Stl': 1.3, 'Blk': 0.4, 'TO': 2.7, 'FG%': .405, '3P%': .363, 'FT%': .800},
    {'Season': '2008-09', 'Team': 'GSW', 'G': 59, 'Min': 39.6, 'Pts': 20.7, 'Reb': 5.1, 'Ast': 6.5, 'Stl': 1.5, 'Blk': 0.5, 'TO': 3.9, 'FG%': .414, '3P%': .338, 'FT%': .826},
    {'Season': '2009-10', 'Team': 'GSW/CHA', 'G': 81, 'Min': 38.6, 'Pts': 20.6, 'Reb': 5.0, 'Ast': 3.7, 'Stl': 1.6, 'Blk': 0.5, 'TO': 3.2, 'FG%': .423, '3P%': .328, 'FT%': .700},
    {'Season': '2010-11', 'Team': 'CHA', 'G': 67, 'Min': 35.9, 'Pts': 18.5, 'Reb': 4.5, 'Ast': 3.6, 'Stl': 1.2, 'Blk': 0.4, 'TO': 3.1, 'FG%': .411, '3P%': .337, 'FT%': .800},
    {'Season': '2011-12', 'Team': 'MIL/SAS', 'G': 47, 'Min': 25.8, 'Pts': 9.8, 'Reb': 3.5, 'Ast': 2.5, 'Stl': 1.1, 'Blk': 0.3, 'TO': 2.2, 'FG%': .374, '3P%': .288, 'FT%': .820},
    {'Season': '2012-13', 'Team': 'SAS', 'G': 55, 'Min': 19.5, 'Pts': 6.2, 'Reb': 2.8, 'Ast': 1.5, 'Stl': 0.7, 'Blk': 0.3, 'TO': 1.4, 'FG%': .373, '3P%': .271, 'FT%': .700},
    {'Season': '2013-14', 'Team': 'LAC', 'G': 9, 'Min': 11.9, 'Pts': 1.7, 'Reb': 1.1, 'Ast': 0.6, 'Stl': 0.7, 'Blk': 0.1, 'TO': 0.7, 'FG%': .231, '3P%': .071, 'FT%': .500}
]

# Convert to DataFrames
manu_df = pd.DataFrame(manu_seasons_rs)
jackson_df = pd.DataFrame(jackson_seasons_rs)
jackson_df['Team_Type'] = jackson_df['Team'].apply(lambda x: 'Spurs' if 'SAS' in x else 'Non-Spurs')

# Calculations for System Variable
jackson_spurs_avg = jackson_df[jackson_df['Team_Type'] == 'Spurs'][['Min', 'Pts', 'Reb', 'Ast', 'Stl', 'TO', 'FG%', '3P%', 'FT%']].mean()
jackson_other_avg = jackson_df[jackson_df['Team_Type'] == 'Non-Spurs'][['Min', 'Pts', 'Reb', 'Ast', 'Stl', 'TO', 'FG%', '3P%', 'FT%']].mean()

comparison_df = pd.DataFrame({
    'Metric': ['Minutes/Game', 'Points/Game', 'Rebounds/Game', 'Assists/Game', 'Steals/Game', 'Turnovers/Game', 'FG%', '3P%', 'FT%'],
    'With Spurs': [jackson_spurs_avg['Min'], jackson_spurs_avg['Pts'], jackson_spurs_avg['Reb'], jackson_spurs_avg['Ast'], jackson_spurs_avg['Stl'], jackson_spurs_avg['TO'], jackson_spurs_avg['FG%'], jackson_spurs_avg['3P%'], jackson_spurs_avg['FT%']],
    'Without Spurs': [jackson_other_avg['Min'], jackson_other_avg['Pts'], jackson_other_avg['Reb'], jackson_other_avg['Ast'], jackson_other_avg['Stl'], jackson_other_avg['TO'], jackson_other_avg['FG%'], jackson_other_avg['3P%'], jackson_other_avg['FT%']]
})
comparison_df['Difference'] = comparison_df['Without Spurs'] - comparison_df['With Spurs']
comparison_df['% Change'] = (comparison_df['Difference'] / comparison_df['With Spurs'] * 100).round(1)

spurs_ast_to = jackson_spurs_avg['Ast'] / jackson_spurs_avg['TO']
other_ast_to = jackson_other_avg['Ast'] / jackson_other_avg['TO']

# Career stats for Verdict
manu_career = {
    'Player': 'Manu Ginobili',
    'Seasons': len(manu_df),
    'Total Games': manu_df['G'].sum(),
    'PPG': (manu_df['Pts'] * manu_df['G']).sum() / manu_df['G'].sum(),
    'RPG': (manu_df['Reb'] * manu_df['G']).sum() / manu_df['G'].sum(),
    'APG': (manu_df['Ast'] * manu_df['G']).sum() / manu_df['G'].sum(),
    'FG%': manu_df['FG%'].mean(),
    '3P%': manu_df['3P%'].mean(),
    'FT%': manu_df['FT%'].mean(),
    'Championships': 4,
    'All-Star': 2,
    'All-NBA': 2,
    '6MOY': 1
}

jackson_career = {
    'Player': 'Stephen Jackson',
    'Seasons': len(jackson_df),
    'Total Games': jackson_df['G'].sum(),
    'PPG': (jackson_df['Pts'] * jackson_df['G']).sum() / jackson_df['G'].sum(),
    'RPG': (jackson_df['Reb'] * jackson_df['G']).sum() / jackson_df['G'].sum(),
    'APG': (jackson_df['Ast'] * jackson_df['G']).sum() / jackson_df['G'].sum(),
    'FG%': jackson_df['FG%'].mean(),
    '3P%': jackson_df['3P%'].mean(),
    'FT%': jackson_df['FT%'].mean(),
    'Championships': 1,
    'All-Star': 0,
    'All-NBA': 0,
    '6MOY': 0
}

# Colors
header_color, spurs_color, other_color = '#2C3E50', '#00594C', '#CE1141'

# ============================================================================
# 1. COMPARISON VISUALIZATION (Comparison Bar Charts)
# ============================================================================
season_2002 = pd.DataFrame({'Player': ['Manu', 'Jackson'], 'Pts/G': [7.6, 11.8], 'FG%': [.438, .435], '3P%': [.345, .320], 'Ast/G': [2.0, 2.3], 'TO/G': [1.4, 2.2], 'Ast/TO': [1.43, 1.05]})
season_2011 = pd.DataFrame({'Player': ['Manu', 'Jackson'], 'Pts/G': [12.9, 8.9], 'FG%': [.526, .405], '3P%': [.413, .306], 'Ast/G': [4.4, 2.0], 'TO/G': [1.9, 1.8], 'Ast/TO': [2.32, 1.11]})
season_2012 = pd.DataFrame({'Player': ['Manu', 'Jackson'], 'Pts/G': [11.8, 6.2], 'FG%': [.425, .373], '3P%': [.353, .271], 'Ast/G': [4.6, 1.5], 'TO/G': [2.2, 1.4], 'Ast/TO': [2.09, 1.07]})

metrics = [('Pts/G', 'Points per Game'), ('FG%', 'Field Goal %'), ('3P%', '3-Point %'), ('Ast/G', 'Assists per Game'), ('TO/G', 'Turnovers per Game'), ('Ast/TO', 'Assist/TO Ratio')]
seasons_comp = ['2002-03', '2011-12', '2012-13']
x = np.arange(len(seasons_comp))
width = 0.25

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Spurs Overlap - Head-to-Head Comparison (2002-03, 2011-12, & 2012-13)', fontsize=16, fontweight='bold')

for idx, (col_name, title) in enumerate(metrics):
    ax = axes[idx // 3, idx % 3]
    manu_vals = [season_2002[col_name][0], season_2011[col_name][0], season_2012[col_name][0]]
    jackson_vals = [season_2002[col_name][1], season_2011[col_name][1], season_2012[col_name][1]]
    ax.bar(x - width/2, manu_vals, width, label='Manu', color='#00594C', alpha=0.9)
    ax.bar(x + width/2, jackson_vals, width, label='Jackson', color='#CE1141', alpha=0.9)
    ax.set_title(title, fontweight='bold', pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(seasons_comp, fontweight='bold')
    if idx == 0: ax.legend()
    ax.grid(axis='y', alpha=0.3)
    for i, (m_val, j_val) in enumerate(zip(manu_vals, jackson_vals)):
        fmt = '{:.1%}' if '%' in title else '{:.1f}'
        if 'Ratio' in title: fmt = '{:.2f}'
        ax.text(i - width/2, m_val, fmt.format(m_val), ha='center', va='bottom', fontsize=8, fontweight='bold')
        ax.text(i + width/2, j_val, fmt.format(j_val), ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig('comparison_visualization.png', dpi=100, bbox_inches='tight')
plt.close()
print("Saved comparison_visualization.png")

# ============================================================================
# 2. SYSTEM VISUALIZATION (Dashboard)
# ============================================================================
fig = plt.figure(figsize=(18, 10))
fig.suptitle('Stephen Jackson - System Variable Analysis\nSpurs vs. Non-Spurs Performance', fontsize=18, fontweight='bold', y=0.98)
gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25)
width = 0.35

# PLOT 1: Volume Stats
ax1 = fig.add_subplot(gs[0, 0])
vol_metrics = ['Minutes', 'Points', 'Rebounds', 'Assists']
spurs_vol = [jackson_spurs_avg['Min'], jackson_spurs_avg['Pts'], jackson_spurs_avg['Reb'], jackson_spurs_avg['Ast']]
other_vol = [jackson_other_avg['Min'], jackson_other_avg['Pts'], jackson_other_avg['Reb'], jackson_other_avg['Ast']]
x = np.arange(len(vol_metrics))
ax1.bar(x - width/2, spurs_vol, width, label='With Spurs', color=spurs_color, alpha=0.85)
ax1.bar(x + width/2, other_vol, width, label='Non-Spurs', color=other_color, alpha=0.85)
for i, v in enumerate(spurs_vol): ax1.text(i - width/2, v + 0.5, f'{v:.1f}', ha='center', fontsize=10, fontweight='bold')
for i, v in enumerate(other_vol): ax1.text(i + width/2, v + 0.5, f'{v:.1f}', ha='center', fontsize=10, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(vol_metrics, fontsize=11, fontweight='bold')
ax1.set_title('Volume Statistics (Per Game)', fontsize=13, fontweight='bold')
ax1.legend()
ax1.grid(axis='y', alpha=0.3, linestyle='--')

# PLOT 2: Efficiency
ax2 = fig.add_subplot(gs[0, 1])
eff_metrics = ['FG%', '3P%', 'FT%']
spurs_eff = [jackson_spurs_avg['FG%'], jackson_spurs_avg['3P%'], jackson_spurs_avg['FT%']]
other_eff = [jackson_other_avg['FG%'], jackson_other_avg['3P%'], jackson_other_avg['FT%']]
x2 = np.arange(len(eff_metrics))
ax2.bar(x2 - width/2, spurs_eff, width, color=spurs_color, alpha=0.85, label='With Spurs')
ax2.bar(x2 + width/2, other_eff, width, color=other_color, alpha=0.85, label='Non-Spurs')
for i, v in enumerate(spurs_eff): ax2.text(i - width/2, v + 0.01, f'{v:.1%}', ha='center', fontsize=10, fontweight='bold')
for i, v in enumerate(other_eff): ax2.text(i + width/2, v + 0.01, f'{v:.1%}', ha='center', fontsize=10, fontweight='bold')
ax2.set_xticks(x2)
ax2.set_xticklabels(eff_metrics, fontsize=11, fontweight='bold')
ax2.set_title('Shooting Efficiency', fontsize=13, fontweight='bold')
ax2.set_ylim(0, 1.0)
ax2.legend()
ax2.grid(axis='y', alpha=0.3, linestyle='--')

# PLOT 3: Ball Control
ax3 = fig.add_subplot(gs[1, 0])
bc_metrics = ['Turnovers/G', 'Ast/TO Ratio']
spurs_bc = [jackson_spurs_avg['TO'], spurs_ast_to]
other_bc = [jackson_other_avg['TO'], other_ast_to]
x3 = np.arange(len(bc_metrics))
ax3.bar(x3 - width/2, spurs_bc, width, color=spurs_color, alpha=0.85, label='With Spurs')
ax3.bar(x3 + width/2, other_bc, width, color=other_color, alpha=0.85, label='Non-Spurs')
for i, v in enumerate(spurs_bc): ax3.text(i - width/2, v + 0.05, f'{v:.2f}', ha='center', fontsize=10, fontweight='bold')
for i, v in enumerate(other_bc): ax3.text(i + width/2, v + 0.05, f'{v:.2f}', ha='center', fontsize=10, fontweight='bold')
ax3.set_xticks(x3)
ax3.set_xticklabels(bc_metrics, fontsize=11, fontweight='bold')
ax3.set_title('Ball Control & Decision Making', fontsize=13, fontweight='bold')
ax3.legend()
ax3.grid(axis='y', alpha=0.3, linestyle='--')

# PLOT 4: Waterfall % Change
ax4 = fig.add_subplot(gs[1, 1])
chg_metrics = ['Minutes', 'Points', 'Rebounds', 'Assists', 'Turnovers']
vals = [comparison_df.loc[i, '% Change'] for i in [0, 1, 2, 3, 5]]
colors_w = ['green' if x > 0 else 'red' for x in vals]
colors_w[4] = 'red' if vals[4] > 0 else 'green'  # Turnovers increasing is bad
bars = ax4.barh(chg_metrics, vals, color=colors_w, alpha=0.7)
ax4.axvline(0, color='black', linewidth=1)
ax4.set_title('Statistical Change Away from Spurs (%)', fontsize=13, fontweight='bold')
for bar, v in zip(bars, vals):
    px = v + 2 if v >= 0 else v - 12
    ax4.text(px, bar.get_y() + bar.get_height()/2, f'{v:+.1f}%', va='center', fontsize=10, fontweight='bold')
ax4.grid(axis='x', alpha=0.3, linestyle='--')

plt.subplots_adjust(left=0.06, right=0.97, top=0.90, bottom=0.08)
plt.savefig('system_visualization.png', dpi=100, bbox_inches='tight')
plt.close()
print("Saved system_visualization.png")

# ============================================================================
# 3. CAREER TIMELINE
# ============================================================================
fig, ax5 = plt.subplots(figsize=(16, 5))
colors_t = [spurs_color if 'SAS' in t else other_color for t in jackson_df['Team']]
ax5.bar(jackson_df['Season'], jackson_df['Pts'], color=colors_t, alpha=0.7)
ax5.plot(jackson_df['Season'], jackson_df['Pts'], 'ko-', markersize=5)
ax5.set_title('Career Scoring Timeline', fontsize=14, fontweight='bold')
ax5.set_ylabel('Points Per Game', fontsize=12)
ax5.tick_params(axis='x', rotation=45)
ax5.axhline(jackson_spurs_avg['Pts'], color=spurs_color, linestyle='--', linewidth=2, label=f"Spurs Avg: {jackson_spurs_avg['Pts']:.1f} ppg")
ax5.axhline(jackson_other_avg['Pts'], color=other_color, linestyle='--', linewidth=2, label=f"Non-Spurs Avg: {jackson_other_avg['Pts']:.1f} ppg")
ax5.legend(loc='upper right', fontsize=11)
ax5.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('career_timeline.png', dpi=100, bbox_inches='tight')
plt.close()
print("Saved career_timeline.png")

# ============================================================================
# 4. SUMMARY TABLE
# ============================================================================
summary_df = pd.DataFrame({
    'Category': ['Volume', 'Volume', 'Volume', 'Volume', 'Efficiency', 'Efficiency', 'Efficiency', 'Efficiency'],
    'Metric': ['Minutes/Game', 'Points/Game', 'Rebounds/Game', 'Assists/Game', 'FG%', '3P%', 'Ast/TO Ratio', 'Turnovers/Game'],
    'Spurs': [f"{jackson_spurs_avg['Min']:.1f}", f"{jackson_spurs_avg['Pts']:.1f}", f"{jackson_spurs_avg['Reb']:.1f}", 
              f"{jackson_spurs_avg['Ast']:.1f}", f"{jackson_spurs_avg['FG%']:.1%}", f"{jackson_spurs_avg['3P%']:.1%}", 
              f"{spurs_ast_to:.2f}", f"{jackson_spurs_avg['TO']:.1f}"],
    'Non-Spurs': [f"{jackson_other_avg['Min']:.1f}", f"{jackson_other_avg['Pts']:.1f}", f"{jackson_other_avg['Reb']:.1f}", 
                  f"{jackson_other_avg['Ast']:.1f}", f"{jackson_other_avg['FG%']:.1%}", f"{jackson_other_avg['3P%']:.1%}", 
                  f"{other_ast_to:.2f}", f"{jackson_other_avg['TO']:.1f}"],
    'Change': [f"+{comparison_df.loc[0, '% Change']:.1f}%", f"+{comparison_df.loc[1, '% Change']:.1f}%", 
               f"+{comparison_df.loc[2, '% Change']:.1f}%", f"+{comparison_df.loc[3, '% Change']:.1f}%",
               f"{comparison_df.loc[6, '% Change']:+.1f}%", f"{comparison_df.loc[7, '% Change']:+.1f}%",
               f"{((other_ast_to-spurs_ast_to)/spurs_ast_to*100):+.1f}%", f"+{comparison_df.loc[5, '% Change']:.1f}%"]
})

fig, ax = plt.subplots(figsize=(14, 5))
ax.axis('off')
table = ax.table(cellText=summary_df.values, colLabels=summary_df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.5, 2.2)
for j in range(len(summary_df.columns)):
    table[(0, j)].set_facecolor('#2C3E50')
    table[(0, j)].set_text_props(weight='bold', color='white')
for i in range(len(summary_df)):
    for j in range(len(summary_df.columns)):
        table[(i+1, j)].set_facecolor('#f8f9fa' if i % 2 == 0 else '#ffffff')

plt.title('Key Findings Summary\n\nCONCLUSION: More opportunities did NOT translate to better efficiency.\nStatistical production increased purely due to higher volume.', 
          fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('summary_visualization.png', dpi=100, bbox_inches='tight')
plt.close()
print("Saved summary_visualization.png")

# ============================================================================
# 5. CAREER TRAJECTORY
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('STEP 3: Career Trajectory Comparison - Manu Ginobili vs Stephen Jackson', fontsize=16, fontweight='bold')

# Plot 1: Points per game over career
axes[0, 0].plot(range(len(manu_df)), manu_df['Pts'], marker='o', label='Manu', color='#00594C', linewidth=2)
axes[0, 0].plot(range(len(jackson_df)), jackson_df['Pts'], marker='s', label='Jackson', color='#CE1141', linewidth=2)
axes[0, 0].set_title('Points Per Game - Career Progression', fontweight='bold')
axes[0, 0].set_xlabel('Season Number')
axes[0, 0].set_ylabel('PPG')
axes[0, 0].legend()
axes[0, 0].grid(alpha=0.3)

# Plot 2: Field Goal % over career
axes[0, 1].plot(range(len(manu_df)), manu_df['FG%'], marker='o', label='Manu', color='#00594C', linewidth=2)
axes[0, 1].plot(range(len(jackson_df)), jackson_df['FG%'], marker='s', label='Jackson', color='#CE1141', linewidth=2)
axes[0, 1].set_title('Field Goal % - Career Progression', fontweight='bold')
axes[0, 1].set_xlabel('Season Number')
axes[0, 1].set_ylabel('FG%')
axes[0, 1].legend()
axes[0, 1].grid(alpha=0.3)
axes[0, 1].set_ylim([0.2, 0.6])

# Plot 3: Assists per game over career
axes[1, 0].plot(range(len(manu_df)), manu_df['Ast'], marker='o', label='Manu', color='#00594C', linewidth=2)
axes[1, 0].plot(range(len(jackson_df)), jackson_df['Ast'], marker='s', label='Jackson', color='#CE1141', linewidth=2)
axes[1, 0].set_title('Assists Per Game - Career Progression', fontweight='bold')
axes[1, 0].set_xlabel('Season Number')
axes[1, 0].set_ylabel('APG')
axes[1, 0].legend()
axes[1, 0].grid(alpha=0.3)

# Plot 4: Career averages comparison (bar chart)
categories = ['PPG', 'RPG', 'APG', 'FG%', '3P%']
manu_avgs = [manu_career['PPG'], manu_career['RPG'], manu_career['APG'], manu_career['FG%'] * 100, manu_career['3P%'] * 100]
jackson_avgs = [jackson_career['PPG'], jackson_career['RPG'], jackson_career['APG'], jackson_career['FG%'] * 100, jackson_career['3P%'] * 100]
x = np.arange(len(categories))
width = 0.35
axes[1, 1].bar(x - width/2, manu_avgs, width, label='Manu', color='#00594C', alpha=0.8)
axes[1, 1].bar(x + width/2, jackson_avgs, width, label='Jackson', color='#CE1141', alpha=0.8)
axes[1, 1].set_title('Career Averages Comparison', fontweight='bold')
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(categories)
axes[1, 1].legend()
axes[1, 1].grid(axis='y', alpha=0.3)
for i, (m, j) in enumerate(zip(manu_avgs, jackson_avgs)):
    axes[1, 1].text(i - width/2, m + 1, f'{m:.1f}', ha='center', fontsize=9)
    axes[1, 1].text(i + width/2, j + 1, f'{j:.1f}', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('career_trajectory.png', dpi=100, bbox_inches='tight')
plt.close()
print("Saved career_trajectory.png")

# ============================================================================
# 6. VERDICT VISUALIZATION
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)
fig.suptitle('COMPREHENSIVE VERDICT: Manu Ginobili vs Stephen Jackson', fontsize=18, fontweight='bold', y=0.98)

# 1. Championships and Awards
ax1 = fig.add_subplot(gs[0, 0])
awards = ['Championships', 'All-Star', 'All-NBA']
manu_awards = [4, 2, 2]
jackson_awards = [1, 0, 0]
x = np.arange(len(awards))
ax1.bar(x - 0.2, manu_awards, 0.4, label='Manu', color='#00594C', alpha=0.8)
ax1.bar(x + 0.2, jackson_awards, 0.4, label='Jackson', color='#CE1141', alpha=0.8)
ax1.set_xticks(x)
ax1.set_xticklabels(awards)
ax1.set_title('Accolades', fontweight='bold')
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# 2. Career Efficiency
ax2 = fig.add_subplot(gs[0, 1])
efficiency = ['FG%', '3P%', 'FT%']
manu_eff = [manu_career['FG%'], manu_career['3P%'], manu_career['FT%']]
jackson_eff = [jackson_career['FG%'], jackson_career['3P%'], jackson_career['FT%']]
x = np.arange(len(efficiency))
ax2.bar(x - 0.2, manu_eff, 0.4, label='Manu', color='#00594C', alpha=0.8)
ax2.bar(x + 0.2, jackson_eff, 0.4, label='Jackson', color='#CE1141', alpha=0.8)
ax2.set_xticks(x)
ax2.set_xticklabels(efficiency)
ax2.set_title('Career Shooting Efficiency', fontweight='bold')
ax2.set_ylim([0, 1])
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# 3. Playoff Games
ax3 = fig.add_subplot(gs[0, 2])
playoff_games = [218, 56]
ax3.bar(['Manu', 'Jackson'], playoff_games, color=['#00594C', '#CE1141'], alpha=0.8)
ax3.set_title('Playoff Games Played', fontweight='bold')
ax3.set_ylabel('Games')
ax3.grid(axis='y', alpha=0.3)
for i, v in enumerate(playoff_games):
    ax3.text(i, v + 5, str(v), ha='center', fontweight='bold')

# 4. Jackson: Spurs vs Other Teams (Minutes)
ax4 = fig.add_subplot(gs[1, 0])
ax4.bar(['With Spurs', 'Other Teams'], [jackson_spurs_avg['Min'], jackson_other_avg['Min']], color=['#00594C', '#CE1141'], alpha=0.8)
ax4.set_title('Jackson: Minutes/Game', fontweight='bold')
ax4.set_ylabel('MPG')
ax4.grid(axis='y', alpha=0.3)

# 5. Jackson: Spurs vs Other Teams (Points)
ax5 = fig.add_subplot(gs[1, 1])
ax5.bar(['With Spurs', 'Other Teams'], [jackson_spurs_avg['Pts'], jackson_other_avg['Pts']], color=['#00594C', '#CE1141'], alpha=0.8)
ax5.set_title('Jackson: Points/Game', fontweight='bold')
ax5.set_ylabel('PPG')
ax5.grid(axis='y', alpha=0.3)

# 6. Jackson: Spurs vs Other Teams (FG%)
ax6 = fig.add_subplot(gs[1, 2])
ax6.bar(['With Spurs', 'Other Teams'], [jackson_spurs_avg['FG%'], jackson_other_avg['FG%']], color=['#00594C', '#CE1141'], alpha=0.8)
ax6.set_title('Jackson: Field Goal %', fontweight='bold')
ax6.set_ylabel('FG%')
ax6.set_ylim([0, 0.5])
ax6.grid(axis='y', alpha=0.3)

# 7. Career trajectory over time
ax7 = fig.add_subplot(gs[2, :])
ax7.plot(manu_df['Season'], manu_df['Pts'], marker='o', label='Manu PPG', color='#00594C', linewidth=2, markersize=6)
ax7.plot(jackson_df['Season'], jackson_df['Pts'], marker='s', label='Jackson PPG', color='#CE1141', linewidth=2, markersize=6)
ax7.set_title('Career Scoring Trajectory (Points Per Game)', fontweight='bold', fontsize=12)
ax7.set_xlabel('Season')
ax7.set_ylabel('PPG')
ax7.legend(loc='upper right')
ax7.grid(alpha=0.3)
ax7.tick_params(axis='x', rotation=45)
ax7.set_xticks(ax7.get_xticks()[::2])

# Highlight Spurs overlap
spurs_seasons = ['2002-03', '2012-13']
for season in spurs_seasons:
    if season in manu_df['Season'].values:
        idx = manu_df[manu_df['Season'] == season].index[0]
        ax7.axvline(x=idx, color='gray', linestyle='--', alpha=0.3, linewidth=1)
        ax7.text(idx, ax7.get_ylim()[1] * 0.95, 'Both on Spurs', rotation=90, verticalalignment='top', fontsize=8, alpha=0.7)

plt.savefig('verdict_visualization.png', dpi=100, bbox_inches='tight')
plt.close()
print("Saved verdict_visualization.png")
