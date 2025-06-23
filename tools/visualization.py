"""visualization.py

記号転位分析の可視化システム
"""

from typing import List, Dict, Any
from .displacement_patterns import DisplacementEvent, PoetryPattern


class DisplacementVisualizer:
    """記号転位可視化器"""
    
    def __init__(self):
        self.pattern_colors = {
            PoetryPattern.EMOTIONAL_EXPRESSION: "#ff6b6b",
            PoetryPattern.NARRATIVE_IDENTIFIER: "#4ecdc4", 
            PoetryPattern.METAPHORICAL_SYNTAX: "#6c5ce7",
            PoetryPattern.SEMANTIC_INVERSION: "#f9ca24",
            PoetryPattern.VISUAL_POETRY: "#45b7d1",
            PoetryPattern.TEMPORAL_EXPRESSION: "#ff7675",
        }
    
    def generate_html_visualization(self, 
                                   poem_id: str,
                                   code_text: str, 
                                   displacements: List[DisplacementEvent],
                                   analysis_report: Dict[str, Any]) -> str:
        """HTML可視化を生成"""
        
        lines = code_text.splitlines()
        
        # 転位を行番号でマッピング
        line_displacements = {}
        for disp in displacements:
            line_num = disp.line_number
            if line_num not in line_displacements:
                line_displacements[line_num] = []
            line_displacements[line_num].append(disp)
        
        # 行ごとのHTMLを生成
        line_htmls = []
        for i, line in enumerate(lines):
            line_disps = line_displacements.get(i, [])
            line_html = self._generate_line_html(i, line, line_disps)
            line_htmls.append(line_html)
        
        # 統計パネルを生成
        stats_html = self._generate_statistics_panel(analysis_report)
        
        return f'''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{poem_id} - 記号転位分析</title>
    <style>{self._get_css()}</style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{poem_id} - コードポエトリー記号転位分析</h1>
            <p>パースの記号分類理論に基づく詩的転位の可視化</p>
        </header>
        
        <div class="main-content">
            <div class="code-panel">
                <h2>Code Poem</h2>
                <div class="code-container">
                    {"".join(line_htmls)}
                </div>
            </div>
            
            <div class="analysis-panel">
                {stats_html}
            </div>
        </div>
    </div>
    
    <script>{self._get_javascript()}</script>
</body>
</html>
        '''
    
    def _generate_line_html(self, line_num: int, line_text: str, 
                           displacements: List[DisplacementEvent]) -> str:
        """単一行のHTMLを生成"""
        
        max_intensity = max([d.intensity for d in displacements], default=0)
        
        # 行のスタイルクラス
        line_classes = ['code-line']
        if max_intensity > 0.8:
            line_classes.append('high-displacement')
        elif max_intensity > 0.6:
            line_classes.append('medium-displacement')  
        elif max_intensity > 0.3:
            line_classes.append('low-displacement')
        
        # 転位をハイライト
        highlighted_line = self._highlight_displacements(line_text, displacements)
        
        # 転位情報
        displacement_info = ""
        if displacements:
            info_items = []
            for disp in displacements:
                color = self.pattern_colors.get(disp.pattern, "#ddd")
                info_items.append(f'''
                <div class="displacement-item" style="border-left-color: {color};">
                    <div class="disp-pattern">{disp.pattern.value}</div>
                    <div class="disp-intensity">強度: {disp.intensity:.2f}</div>
                    <div class="disp-description">{disp.description}</div>
                </div>
                ''')
            displacement_info = f'<div class="displacement-list">{"".join(info_items)}</div>'
        
        return f'''
        <div class="line-container {' '.join(line_classes)}" data-line="{line_num}">
            <div class="line-main">
                <span class="line-number">{line_num + 1:3d}</span>
                <span class="line-content">{highlighted_line}</span>
                <div class="intensity-bar">
                    <div class="bar-fill" style="width: {max_intensity * 100}%; 
                         background: {self._get_intensity_color(max_intensity)};"></div>
                </div>
            </div>
            <div class="line-details">
                {displacement_info}
            </div>
        </div>
        '''
    
    def _highlight_displacements(self, line_text: str, 
                                displacements: List[DisplacementEvent]) -> str:
        """行内の転位をハイライト"""
        if not displacements:
            return self._escape_html(line_text)
        
        highlighted = self._escape_html(line_text)
        for disp in displacements:
            if disp.node_text in line_text:
                pattern_class = f"displacement {disp.pattern.value}"
                color = self.pattern_colors.get(disp.pattern, "#ddd")
                
                highlighted = highlighted.replace(
                    self._escape_html(disp.node_text),
                    f'<span class="{pattern_class}" style="border-bottom-color: {color};" '
                    f'title="{self._escape_html(disp.description)}">'
                    f'{self._escape_html(disp.node_text)}</span>'
                )
        
        return highlighted
    
    def _generate_statistics_panel(self, analysis_report: Dict[str, Any]) -> str:
        """統計パネルを生成"""
        
        total = analysis_report.get('total_displacements', 0)
        if total == 0:
            return '''
            <div class="statistics-panel">
                <h3>分析結果</h3>
                <p>詩的転位が検出されませんでした。</p>
            </div>
            '''
        
        max_intensity = analysis_report.get('max_intensity', 0)
        avg_intensity = analysis_report.get('avg_intensity', 0)
        
        # パターン別統計
        pattern_stats = ""
        patterns = analysis_report.get('pattern_distribution', {})
        for pattern_name, stats in patterns.items():
            color = self.pattern_colors.get(
                PoetryPattern(pattern_name), "#ddd"
            )
            percentage = (stats['count'] / total) * 100
            
            pattern_stats += f'''
            <div class="pattern-stat">
                <div class="pattern-info">
                    <span class="pattern-color" style="background: {color};"></span>
                    <span class="pattern-name">{pattern_name}</span>
                </div>
                <div class="pattern-count">{stats['count']}回 ({percentage:.1f}%)</div>
            </div>
            '''
        
        # 詩的解釈
        interpretation = analysis_report.get('poetic_interpretation', '')
        
        return f'''
        <div class="statistics-panel">
            <h3>分析統計</h3>
            <div class="summary-stats">
                <div class="stat-item">
                    <span class="stat-label">総転位数</span>
                    <span class="stat-value">{total}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">最大強度</span>
                    <span class="stat-value">{max_intensity:.2f}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">平均強度</span>
                    <span class="stat-value">{avg_intensity:.2f}</span>
                </div>
            </div>
            
            <h4>パターン分布</h4>
            <div class="pattern-stats">
                {pattern_stats}
            </div>
            
            <h4>詩的解釈</h4>
            <div class="interpretation">
                <pre>{interpretation}</pre>
            </div>
        </div>
        '''
    
    def _get_intensity_color(self, intensity: float) -> str:
        """強度に応じた色を取得"""
        if intensity >= 0.8:
            return "#d63031"
        elif intensity >= 0.6:
            return "#e84393"
        elif intensity >= 0.4:
            return "#fdcb6e"
        elif intensity >= 0.2:
            return "#74b9ff"
        else:
            return "#ddd"
    
    def _escape_html(self, text: str) -> str:
        """HTMLエスケープ"""
        return (text.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;'))
    
    def _get_css(self) -> str:
        """CSSスタイル"""
        return '''
        * { box-sizing: border-box; }
        body { 
            font-family: 'Monaco', 'Menlo', monospace; 
            margin: 0; background: #f8f9fa; color: #2d3436; 
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        header { text-align: center; margin-bottom: 30px; }
        header h1 { color: #2d3436; margin-bottom: 10px; }
        header p { color: #636e72; }
        
        .main-content { display: flex; gap: 30px; }
        .code-panel { flex: 2; }
        .analysis-panel { flex: 1; }
        
        .code-container { 
            background: white; border-radius: 8px; 
            box-shadow: 0 2px 10px rgba(0,0,0,0.1); padding: 20px; 
        }
        
        .line-container { 
            margin-bottom: 8px; border-radius: 4px;
            transition: all 0.2s; cursor: pointer;
        }
        .line-container:hover { background: rgba(116, 185, 255, 0.1); }
        
        .line-main {
            display: flex; align-items: center; padding: 4px 0;
        }
        .line-number { 
            width: 40px; color: #b2bec3; text-align: right; 
            margin-right: 15px; user-select: none; 
        }
        .line-content { flex: 1; margin-right: 15px; }
        
        .intensity-bar { 
            width: 60px; height: 12px; background: #eee; 
            border-radius: 6px; overflow: hidden;
        }
        .bar-fill { height: 100%; transition: width 0.3s; }
        
        .line-details {
            margin-left: 55px; margin-top: 8px; display: none;
        }
        .line-container.expanded .line-details { display: block; }
        
        .displacement-list { }
        .displacement-item { 
            margin-bottom: 8px; padding: 8px; background: #f8f9fa; 
            border-radius: 4px; border-left: 3px solid #ddd;
            font-size: 0.9em;
        }
        .disp-pattern { font-weight: bold; color: #2d3436; }
        .disp-intensity { color: #666; margin: 2px 0; }
        .disp-description { color: #666; font-size: 0.85em; }
        
        /* 転位強度による行スタイル */
        .high-displacement { border-left: 3px solid #d63031; }
        .medium-displacement { border-left: 3px solid #e84393; }
        .low-displacement { border-left: 3px solid #fdcb6e; }
        
        /* 転位ハイライト */
        .displacement {
            padding: 2px 4px; border-radius: 3px; font-weight: bold;
            cursor: help; transition: all 0.2s;
            border-bottom: 2px solid;
            background: rgba(255, 255, 255, 0.3);
        }
        .displacement:hover { transform: scale(1.05); }
        
        /* 統計パネル */
        .statistics-panel {
            background: white; border-radius: 8px; 
            box-shadow: 0 2px 10px rgba(0,0,0,0.1); padding: 20px;
        }
        .summary-stats { margin-bottom: 20px; }
        .stat-item { 
            display: flex; justify-content: space-between; 
            margin-bottom: 8px; padding: 8px; background: #f8f9fa; 
            border-radius: 4px;
        }
        .stat-label { font-weight: bold; }
        .stat-value { color: #666; }
        
        .pattern-stats { margin-bottom: 20px; }
        .pattern-stat { 
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 8px; padding: 8px; background: #f8f9fa; 
            border-radius: 4px;
        }
        .pattern-info { display: flex; align-items: center; }
        .pattern-color { 
            width: 12px; height: 12px; border-radius: 2px; 
            margin-right: 8px; 
        }
        .pattern-name { font-weight: bold; }
        .pattern-count { color: #666; }
        
        .interpretation { 
            background: #f8f9fa; padding: 15px; border-radius: 4px;
            border-left: 3px solid #74b9ff;
        }
        .interpretation pre { 
            margin: 0; font-family: inherit; white-space: pre-wrap; 
            line-height: 1.4;
        }
        '''
    
    def _get_javascript(self) -> str:
        """JavaScript"""
        return '''
        document.addEventListener('DOMContentLoaded', function() {
            // 行クリックで詳細表示/非表示
            document.querySelectorAll('.line-container').forEach(function(line) {
                line.addEventListener('click', function() {
                    this.classList.toggle('expanded');
                });
            });
        });
        '''