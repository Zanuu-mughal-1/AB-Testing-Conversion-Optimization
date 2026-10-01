from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from scipy.stats import norm
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
df=pd.read_csv(ROOT/'data/experiment.csv'); g=df.groupby('variant').agg(visitors=('visitor_id','count'),conversions=('converted','sum'),revenue=('revenue','sum')); g['conversion_rate']=g.conversions/g.visitors; g['revenue_per_visitor']=g.revenue/g.visitors
c=g.loc['Control']; t=g.loc['Treatment']; pooled=(c.conversions+t.conversions)/(c.visitors+t.visitors); se=np.sqrt(pooled*(1-pooled)*(1/c.visitors+1/t.visitors)); z=(t.conversion_rate-c.conversion_rate)/se; p=2*(1-norm.cdf(abs(z)))
se_diff=np.sqrt(c.conversion_rate*(1-c.conversion_rate)/c.visitors+t.conversion_rate*(1-t.conversion_rate)/t.visitors); diff=t.conversion_rate-c.conversion_rate; ci=(diff-1.96*se_diff,diff+1.96*se_diff); uplift=100*diff/c.conversion_rate
result=pd.DataFrame([{'control_rate':c.conversion_rate,'treatment_rate':t.conversion_rate,'absolute_lift':diff,'relative_uplift_pct':uplift,'z_score':z,'p_value':p,'ci95_low':ci[0],'ci95_high':ci[1],'statistically_significant':p<.05,'recommendation':'Ship treatment' if p<.05 and diff>0 else 'Keep collecting data'}]); result.to_csv(OUT/'experiment_result.csv',index=False); g.to_csv(OUT/'variant_summary.csv')
plt.figure(figsize=(5,4)); plt.bar(g.index,g.conversion_rate*100); plt.ylabel('Conversion Rate (%)'); plt.title('A/B Test Conversion'); plt.tight_layout(); plt.savefig(OUT/'conversion_comparison.png',dpi=160); plt.close()
print(g.round(4)); print(result.round(4).to_string(index=False))
