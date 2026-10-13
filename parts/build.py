import json, os, re
base = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(base)
order = ['01-head.html', '02-stage-css.html', '03-body.html', '04-js-core.html', '04b-i18n.html', '05-js-scroller-voice.html', '06-js-actions.html', '07-js-views.html']
html = ''.join(open(os.path.join(base, f), encoding='utf-8').read() for f in order)
samples = {}
for lang in ('pt', 'en', 'es'):
    samples[lang] = open(os.path.join(root, 'scripts', f'roteiro.{lang}.md'), encoding='utf-8').read()
inject = 'const SAMPLES = ' + json.dumps(samples, ensure_ascii=False) + ';'
assert '/*__SAMPLES__*/' in html
html = html.replace('/*__SAMPLES__*/', inject)
open(os.path.join(root, 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html:', len(html), 'bytes')
