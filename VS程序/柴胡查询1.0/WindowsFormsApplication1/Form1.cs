using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data;
using System.Data.SqlClient;

namespace WindowsFormsApplication1
{
    public partial class 柴胡数据查询导出系统 : Form
    {
        public 柴胡数据查询导出系统()
        {
            InitializeComponent();
        }
        private string userName = "sa";
        private string password = "YXW19941029";
        private string server = "172.16.1.121";
        //private string server = "124.200.37.90";
        private string connStr = "";
        private string sqlvar = "";
        private string sql = "";
        public SqlConnection conn = null;
        int count = 1;
        private void button1_Click(object sender, EventArgs e)
        {
            if (count == 1)
            {
                sqlvar = "方剂药物组成 like '%" + text0.Text + "%' ";
            }
            else
            {
                for (int i = 0; i <count; i++)
                {
                    if (i == 0)
                    {
                        sqlvar += "  方剂药物组成 like '%" + ((TextBox)(this.Controls.Find("text" + i.ToString(), false)[0])).Text + "%' ";
                    }
                    else
                    {
                        sqlvar += "  and 方剂药物组成 like '%" + ((TextBox)(this.Controls.Find("text" + i.ToString(), false)[0])).Text + "%' ";
                    }
                }
            }
            string id = textBox1.Text.ToString().Trim();
            //string medicine1 = textbox2.text.tostring().trim();
            try
            {
                connStr = "server=" + server + ";uid=" + userName + ";pwd=" + password + ";database=gxbdb";
                conn = new SqlConnection(connStr);
                conn.Open();
                if (id == "")
                {
                    sql = "select * from main where " + sqlvar;
                }
                else
                {
                    sql = "select * from main where id=" + id + " and "+sqlvar;
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
                sql = "";
                sqlvar = "";
            }
            catch (Exception se)
            {
                MessageBox.Show("不能连接数据库，详细信息如下\n" + se.ToString());
            }
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!(Char.IsNumber(e.KeyChar)) && e.KeyChar != (char)8)
            {
                e.Handled = true;
            }
        }

        int x = 113, y = 60;
        private void button2_Click(object sender, EventArgs e)
        {
            if (count <= 10)
            {
                int x1;
                TextBox text = new TextBox();
                text.Name = "text" + count.ToString();
                x1 = x + count * 83;
                text.Location = new Point(x1, y);
                text.Height = 21;
                text.Width = 63;
                this.Controls.Add(text);
                TextBox text1 = new TextBox();
                text1.Name = "text" + count.ToString()+count.ToString();
                text1.Location = new Point(x1, y+30);
                text1.Height = 21;
                text1.Width = 63;
                this.Controls.Add(text1);
                TextBox text2 = new TextBox();
                text2.Name = "text" + count.ToString() + count.ToString() + count.ToString();
                text2.Location = new Point(x1, y+60);
                text2.Height = 21;
                text2.Width = 63;
                this.Controls.Add(text2);
                TextBox text3 = new TextBox();
                text3.Name = "text" + count.ToString() + count.ToString() + count.ToString() + count.ToString();
                text3.Location = new Point(x1, y + 90);
                text3.Height = 21;
                text3.Width = 63;
                this.Controls.Add(text3);
                count++;
                button2.Location = new Point(x1 + 88, y);
                button4.Location = new Point(x1 + 169, y);
            }
            else 
            {
                MessageBox.Show("不可添加了");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            
            if (count == 1)
            {
                sqlvar = "(药名 ='" + text0.Text + "' ";
                if (text00.Text.Trim() != "")
                {
                    sqlvar += " and 药量=" + Convert.ToDouble(text00.Text.Trim());
                }
                if (text000.Text.Trim() != "")
                {
                    sqlvar += " and 单位='" + text000.Text.Trim()+"'";
                }
                if (text0000.Text.Trim() != "")
                {
                    sqlvar += " and 朝代='" + text0000.Text.Trim() + "'";
                }
                sqlvar += ")";
            }              
            else
            {       
                for (int i = 0; i < count; i++)
                {
                    
                    if (i == 0)
                    {
                        sqlvar += " (药名 ='" + ((TextBox)(this.Controls.Find("text" + i.ToString(), false)[0])).Text + "' ";
                        if (((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString(), false)[0])).Text.Trim() != "")
                        {
                            sqlvar += " and 药量=" + Convert.ToDouble(((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString(), false)[0])).Text.Trim());
                        }
                        if (((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString() + i.ToString(), false)[0])).Text.Trim() != "")
                        {
                            sqlvar += " and 单位=" + Convert.ToDouble(((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString() + i.ToString(), false)[0])).Text.Trim());
                        }
                        if (((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString() + i.ToString() + i.ToString(), false)[0])).Text.Trim() != "")
                        {
                            sqlvar += " and 朝代=" + Convert.ToDouble(((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString() + i.ToString() + i.ToString(), false)[0])).Text.Trim());
                        }
                        sqlvar += ")";

                    }
                    else
                    {
                        sqlvar += " or (药名 = '%" + ((TextBox)(this.Controls.Find("text" + i.ToString(), false)[0])).Text + "' ";
                        if (((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString(), false)[0])).Text.Trim() != "")
                        {
                            sqlvar += " and 药量=" + Convert.ToDouble(((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString(), false)[0])).Text.Trim());
                        }
                        if (((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString() + i.ToString(), false)[0])).Text.Trim() != "")
                        {
                            sqlvar += " and 单位=" + Convert.ToDouble(((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString() + i.ToString(), false)[0])).Text.Trim());
                        }
                        if (((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString() + i.ToString() + i.ToString(), false)[0])).Text.Trim() != "")
                        {
                            sqlvar += " and 朝代=" + Convert.ToDouble(((TextBox)(this.Controls.Find("text" + i.ToString() + i.ToString() + i.ToString() + i.ToString(), false)[0])).Text.Trim());
                        }
                        sqlvar += ")";
                    }
                    
                }
            }
            string id = textBox1.Text.ToString().Trim();
            //string medicine1 = textbox2.text.tostring().trim();
            try
            {
                int flat = 0;
                for (int i = 0; i < count; i++)
                {
                    if (((TextBox)(this.Controls.Find("text" + i.ToString(), false)[0])).Text.Trim() == "" && count !=1)
                    {
                        flat = 1;
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
                    if (id == "")
                    {
                        sql = "select * from newmain where " + sqlvar;
                    }
                    else
                    {
                        sql = "select * from newmain where id=" + id + " and " + sqlvar;
                    }
                    //sql = "select * from main";
                    textBox2.Text = sql;
                    SqlCommand sc = new SqlCommand(sql, conn);
                    SqlDataAdapter sda = new SqlDataAdapter(sc);
                    DataSet ds = new DataSet();
                    sda.Fill(ds, "main");
                    dataGridView1.DataSource = ds;
                    dataGridView1.DataMember = "main";
                    conn.Close();
                    conn.Dispose();     
                }
                sql = "";
                sqlvar = "";

            }
            catch (Exception se)
            {
                MessageBox.Show("不能连接数据库，详细信息如下\n" + se.ToString());
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (count == 1)
            {
                MessageBox.Show("不可删除了");
            }
            else
            {
                count--;
                ((TextBox)(this.Controls.Find("text" + count.ToString(), false)[0])).Dispose();
                ((TextBox)(this.Controls.Find("text" + count.ToString() + count.ToString(), false)[0])).Dispose();
                ((TextBox)(this.Controls.Find("text" + count.ToString() + count.ToString() + count.ToString(), false)[0])).Dispose();
                ((TextBox)(this.Controls.Find("text" + count.ToString() + count.ToString() + count.ToString() + count.ToString(), false)[0])).Dispose();
                int x1 = button2.Location.X;
                button2.Location = new Point(x1 - 83, y);
                button4.Location = new Point(x1 - 83 + 81, y);
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string str="";
            int row = dataGridView1.RowCount;
            if (row == 0)
            { MessageBox.Show("无表转化"); }
            else
            {
                string[] a = new string[row - 1];
                for (int i = 0; i < row - 1; i++)
                {
                    a[i] = dataGridView1.Rows[i].Cells[0].Value.ToString().Trim();
                }
                Form2 fom = new Form2(a,1);
                fom.Show();
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string str = "";
            int row = dataGridView1.RowCount;
            if (row == 0)
            { MessageBox.Show("无表转化"); }
            else
            {
                string[] a = new string[row - 1];
                for (int i = 0; i < row - 1; i++)
                {
                    a[i] = dataGridView1.Rows[i].Cells[0].Value.ToString().Trim();
                }
                Form2 fom = new Form2(a, 0);
                fom.Show();
            }
        }
    }
}
