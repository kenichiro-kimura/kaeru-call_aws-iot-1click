# AWS IoT 1-click Button��Ȥä������륳����

## ����

�Ȥ˵������ˤϡ���²�˥����륳����򤷤ޤ���͡�(�����Ϥ��ޤ�)

�Ť�������(������֥������)���ݥ��٥롢�᡼��ʤɤȻ���������ȶ��ˤ��μ��ʤ��Ѥ�äƤ��ƺǶ��LINE��Ȥ��륱������¿���ΤǤϤʤ��Ǥ��礦����

��������˻�����Ȥɤ����Ƥ�ֵ���͡סֶ����٤��ʤ��פΤ��ä�������ǤĤ��������ݤ��ä���˺�줿�ꤷ�ޤ���

�����ǡ��ܥ���1����å��Ǥ���������гڤˤʤ�Τ��ʤȺ�ä��Τ����Υץ��������Ȥˤʤ�ޤ���

�ܥ��󥯥�å����ֵ���͡ס����֥륯��å����ֵޤ��ǵ���͡ס����󥰥���å����֤�����٤��ʤ�פ��б����Ƥ��ꡢLINE�Υ��롼��������Ƥ���ޤ���
��������å�������CG�򿧡��Ѥ���С������륳����ʳ������Ӥˤ�Ȥ��ޤ���

## �Ȥ�������

AWS�Υ�������Ȥκ�����ʤɤξܺ٤�Ŭ��Ĵ�٤Ƥ���������

- python2.7�򥤥󥹥ȡ��뤹��
- AWS�Υ�������Ȥ��ꡢaws cli��ư���褦�ˤ���
- [������](https://aws.amazon.com/jp/iot-1-click/devices/)�򸫤ƥǥХ��������ꤹ��
  - �Ŀ�Ū�ˤ���³����ñ�����Ӥ��Ѥ�����[SORACOM LTE-M Button powered by AWS](https://pages.soracom.jp/LP_SORACOM-LTE-M-Button.html)��������Ǥ���
- ���Υץ��������Ȥ�git clone����
- serverless framework�򥤥󥹥ȡ��뤹��
  ```bash
  %pip install serverless
  ```
- ɬ�פʥ饤�֥��������
  ```bash
  %pip install -r requirements.txt -t ./
  ```
- ����å������Ȥ���LINE��������CG��3������������ɤ���https�ǥ��������Ǥ���Ȥ������֤���URL�ȥե�����̾��config.ini�˵��ܤ���
- ��ꤢ�����ǥץ�������
  ```bash
  %sls deploy
  ```
- LINE Messaging API��Developer Trial(̵��)����󤷤ƥܥåȥ�������Ȥ���
- �ǥץ�������ɽ�����줿API Gateway��URL��Messaging API�Υ�����Хå�����Ͽ����
- �ܥåȥ�������Ȥ�LINE��ͧã�ˤʤꡢŬ���ʥ��롼�פ�������Ƥ����˾��Ԥ���
- AWS�Υ��󥽡��뤫�顢Lambda�ؿ���kaeru-call-hello-dev�פ�CloudWatch Logs�򸫤�ȥ��롼�׾��ԤΥ��٥�ȥ������ФƤ�Ϥ��ʤΤǡ�groupId�פ���ʬ���������config.ini�˵��ܤ���
- sls
- �⤦1��ǥץ�������
  ```bash
  %sls deploy
  ```
- �ܥ����Ҥ�Ť���
  - AWS�Υ��󥽡���ʤ�����CLI�ǡ��������줿Lambda�ؿ���kaeru-call-sendmsg-dev�פ˥ܥ����Ҥ�Ť���


 