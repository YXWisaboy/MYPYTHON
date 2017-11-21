using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace WindowsFormsApplication1
{
    public partial class Form2 : Form
    {
        int f;
        private string userName = "sa";
        private string password = "YXW19941029";
        private string server = "172.16.1.121";
        //private string server = "124.200.37.90";
        private string connStr = "";
        private string sqlvar = "";
        private string sql = "";
        public SqlConnection conn = null;
        string[] arr;
        public Form2(string[] a,int f)
        {
            InitializeComponent();
            arr=GetString(a);
            this.f = f;
        }
        public  string[] GetString(string[] values)
        {
            List<string> list = new List<string>();
            for (int i = 0; i < values.Length; i++)//遍历数组成员
            {
                if (list.IndexOf(values[i].ToLower()) == -1)//对每个成员做一次新数组查询如果没有相等的则加到新数组
                    list.Add(values[i]);
            }
            return list.ToArray();
        }
        private void Form2_Load(object sender, EventArgs e)
        {
            try
            {
                int flat = 0;
                for (int i = 0; i < arr.Length; i++)
                {
                    if (i == 0)
                    {
                        sqlvar += " id=" + Convert.ToDouble(arr[i]);
                    }
                    else
                    {
                        sqlvar += " or id=" + Convert.ToDouble(arr[i]);
                    }

                }
                if (flat == 1)
                {
                    MessageBox.Show("添加的药物名不能为空");
                }
                else
                {
                    connStr = "server=" + server + ";uid=" + userName + ";pwd=" + password + ";database=gxbdb";
                    conn = new SqlConnection(connStr);
                    conn.Open();
                    if (f == 1)
                    {
                        sql = "select * from newmain where " + sqlvar;
                    }
                    else if (f == 0)
                    {
                        sql = "select * from main where " + sqlvar;
                    }
                  

                    //sql = "select * from main";

                    SqlCommand sc = new SqlCommand(sql, conn);
                    SqlDataAdapter sda = new SqlDataAdapter(sc);
                    DataSet ds = new DataSet();
                    sda.Fill(ds, "main");
                    dataGridView1.DataSource = ds;
                    dataGridView1.DataMember = "main";
                    conn.Close();
                    conn.Dispose();
                }

            }
            catch (Exception se)
            {
                MessageBox.Show("不能连接数据库，详细信息如下\n" + se.ToString());
            }
        }

    
    }
}
