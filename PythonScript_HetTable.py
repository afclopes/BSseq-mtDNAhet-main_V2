#! usr/bin/env/ python

import pandas as pd
import numpy as np
from pathlib import Path



value_table={}

def heteroplasmies(table):
    for row in range(len(table)):
       if table.iloc[row]['REF']=='G' and table.iloc[row]['ALT']=='A':
          if table.iloc[row]['DP4-Ref-Fwd'] == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=(table.iloc[row]['DP4-Alt-Fwd']/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Alt-Fwd']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='G' and table.iloc[row]['ALT']=='T':
          if table.iloc[row]['DP4-Ref-Fwd'] == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=(table.iloc[row]['DP4-Alt-Fwd']/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Alt-Fwd']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='G' and table.iloc[row]['ALT']=='C':
             value='No Distinction'
             value_table[row]=value

       elif table.iloc[row]['REF']=='G' and table.iloc[row]['ALT']=='.':
          if (table.iloc[row]['DP4-Alt-Rev'] + table.iloc[row]['DP4-Alt-Fwd']) == 0:
             value='No ALT'
             value_table[row]=value
          else:
             value=((table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev'])/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value



       elif table.iloc[row]['REF']=='C' and table.iloc[row]['ALT']=='A':
          if table.iloc[row]['DP4-Ref-Rev'] == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=(table.iloc[row]['DP4-Alt-Rev']/(table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='C' and table.iloc[row]['ALT']=='T':
          if table.iloc[row]['DP4-Ref-Rev'] == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=(table.iloc[row]['DP4-Alt-Rev']/(table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='C' and table.iloc[row]['ALT']=='G':
             value='No Distinction'
             value_table[row]=value

       elif table.iloc[row]['REF']=='C' and table.iloc[row]['ALT']=='.':
          if (table.iloc[row]['DP4-Alt-Rev'] + table.iloc[row]['DP4-Alt-Fwd']) == 0:
             value='No ALT'
             value_table[row]=value
          else:
             value=((table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev'])/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value


       elif table.iloc[row]['REF']=='T' and table.iloc[row]['ALT']=='A':
          if (table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Ref-Fwd']) == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=((table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev'])/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='T' and table.iloc[row]['ALT']=='C':
          if table.iloc[row]['DP4-Ref-Rev'] == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=(table.iloc[row]['DP4-Alt-Rev']/( table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='T' and table.iloc[row]['ALT']=='G':
          if table.iloc[row]['DP4-Ref-Fwd'] == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=(table.iloc[row]['DP4-Alt-Fwd']/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Alt-Fwd']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='T' and table.iloc[row]['ALT']=='.':
          if (table.iloc[row]['DP4-Alt-Rev'] + table.iloc[row]['DP4-Alt-Fwd']) == 0:
             value='No ALT'
             value_table[row]=value
          else:
             value=((table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev'])/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value



       elif table.iloc[row]['REF']=='A' and table.iloc[row]['ALT']=='T':
          if (table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Ref-Fwd']) == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=((table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev'])/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='A' and table.iloc[row]['ALT']=='G':
          if table.iloc[row]['DP4-Ref-Fwd'] == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=(table.iloc[row]['DP4-Alt-Fwd']/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Alt-Fwd'] ))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='A' and table.iloc[row]['ALT']=='C':
          if table.iloc[row]['DP4-Ref-Rev'] == 0:
             value='No Ref'
             value_table[row]=value
          else:
             value=(table.iloc[row]['DP4-Alt-Rev']/( table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value

       elif table.iloc[row]['REF']=='A' and table.iloc[row]['ALT']=='.':
          if (table.iloc[row]['DP4-Alt-Rev'] + table.iloc[row]['DP4-Alt-Fwd']) == 0:
             value='No ALT'
             value_table[row]=value
          else:
             value=((table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev'])/(table.iloc[row]['DP4-Ref-Fwd'] + table.iloc[row]['DP4-Ref-Rev'] + table.iloc[row]['DP4-Alt-Fwd'] + table.iloc[row]['DP4-Alt-Rev']))*100
             value_table[row]=value


for path in Path('/path/to/directory/with/finalvcffiles').glob('*_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_final.vcf'):

        #read table with header
        PE_MAPQ20_table=pd.read_table(str(path),sep="\s+",header='infer')
        print("Originial table")
        print(PE_MAPQ20_table.head(5))
        print(PE_MAPQ20_table.shape)

        #calculate heteroplasmy approximation
        heteroplasmies(PE_MAPQ20_table)


        het=value_table

        het_table=pd.DataFrame.from_dict(het,orient='index')

        het_table=het_table.rename({0:"Het_Approx"},axis='columns')

        final_table=PE_MAPQ20_table.join(het_table,how="outer")
        print("Original table plus heteroplasmy approximation")
        print(final_table.head(5))
        print(final_table.shape)

        #calculate total reads per base
        final_table['Total_Reads']=final_table['DP4-Ref-Fwd']+final_table['DP4-Ref-Rev']+final_table['DP4-Alt-Fwd']+final_table['DP4-Alt-Rev']
        print("Previous table plus total reads per base")
        print(final_table.head())
        print(final_table.shape)

        #calculate total alternative reads per base
        final_table['Total_Alt']=final_table['DP4-Alt-Fwd']+final_table['DP4-Alt-Rev']
        print("Previous table plus total alternative reads per base")
        print(final_table.head())
        print(final_table.shape)

        #remove bases with less than 5 reads
        final_table_Tot5=final_table[final_table['Total_Reads']>5]
        print("New table with minimum of 5 reads per base")
        print(final_table_Tot5.head(10))
        print(final_table_Tot5.shape)

        #remove rows with <=5 alternative reads, if an alternative base is found
        final_table_Tot5_Alt5= final_table_Tot5.drop(final_table_Tot5[(final_table_Tot5.ALT!= ".") & (final_table_Tot5.Total_Alt < 5)].index)
        print("New table with alternative bases covered by at least 5 bases")
        print(final_table_Tot5_Alt5.head(10))
        print(final_table_Tot5_Alt5.shape)

        #remove rows where an alternative base is found but is not supported by forward and reverse strand
        final_table_Tot5_Alt5_AltFwdRev=final_table_Tot5_Alt5.drop(final_table_Tot5_Alt5[(final_table_Tot5_Alt5.ALT!=".") & (final_table_Tot5_Alt5["DP4-Alt-Fwd"] <1) & (final_table_Tot5_Alt5["DP4-Alt-Rev"] <1)].index)
        print("New table with alternative bases supported by at least 1 read per strand")
        print(final_table_Tot5_Alt5_AltFwdRev.head(10))
        print(final_table_Tot5_Alt5_AltFwdRev.shape)

        #remove rows where there is no alternative base but there are alternative reads above 5
        final_table_Tot5_Alt5_AltFwdRev_RefORAlt5=final_table_Tot5_Alt5_AltFwdRev.drop(final_table_Tot5_Alt5_AltFwdRev[(final_table_Tot5_Alt5_AltFwdRev.ALT==".") & ((final_table_Tot5_Alt5["DP4-Alt-Fwd"] >=5) | (final_table_Tot5_Alt5["DP4-Alt-Rev"] >=5))].index)
        print("New table without alternative bases but with alternative reads above 5")
        print(final_table_Tot5_Alt5_AltFwdRev_RefORAlt5.head(10))
        print(final_table_Tot5_Alt5_AltFwdRev_RefORAlt5.shape)

        #remove rows that have QUAL<20
        final_table_Tot5_Alt5_AltFwdRev_RefORAlt5_QUAL20=final_table_Tot5_Alt5_AltFwdRev_RefORAlt5.drop(final_table_Tot5_Alt5_AltFwdRev_RefORAlt5[(final_table_Tot5_Alt5_AltFwdRev_RefORAlt5.QUAL<20)].index)
        print("New table with only quality above 20")
        print(final_table_Tot5_Alt5_AltFwdRev_RefORAlt5_QUAL20.head(10))
        print(final_table_Tot5_Alt5_AltFwdRev_RefORAlt5_QUAL20.shape)

        #specify the output path for the files produced
        output_path=path.with_name(path.stem + '_python.csv')

        #write table
        final_table_Tot5_Alt5_AltFwdRev_RefORAlt5_QUAL20.to_csv(str(output_path),sep="\t",header=True)


