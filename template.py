EMAIL_SIGNATURE_TEMPLATE = """
<div dir="ltr">
<table style="direction:ltr;border-collapse:collapse;">
<tr><td style="font-size:0;height:12px;line-height:0;"></td></tr>
<tr><td>
  <table cellpadding="0" cellspacing="0" border="0" style="width:100%;">
    <tr>
      <td>
        <table cellpadding="0" cellspacing="0" style="border-collapse:collapse;line-height:1.15;">
          <tr>
            <!-- Logo -->
            <td style="vertical-align:middle;padding:.01px 12px 0.01px 1px;width:130px;text-align:center;">
              <p style="margin:1px">
                <a href="{company_website}" style="display:block;font-size:.1px" target="_blank" rel="nofollow noreferrer">
                  <img border="0" src="{logo_url}" height="83" width="130" alt="logo" style="width:130px;vertical-align:middle;border-radius:0;height:83px;border:0;display:block;">
                </a>
              </p>
            </td>
            <!-- Details -->
            <td valign="top" style="padding:.01px 0.01px 0.01px 12px;vertical-align:top;border-left:solid 1px #BDBDBD;">
              <table cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
                <tr>
                  <td style="padding:.01px;">
                    <p style="margin:.1px;line-height:108.0%;font-size:14px;">
                      <span style="font-family:Arial;font-size:14px;font-weight:bold;color:#646464;letter-spacing:0;white-space:nowrap;">{name}</span><br>
                      <span style="font-family:Arial;font-size:11px;font-weight:bold;color:#646464;white-space:nowrap;">{title}</span>
                    </p>
                  </td>
                </tr>
                <tr>
                  <td style="height:0;">
                    <table cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
                      <tr>
                        <!-- Phone -->
                        <td nowrap width="86" style="height:0;padding-top:12px;white-space:nowrap;width:86px;font-family:Arial;">
                          <p style="margin:1px;line-height:99%;font-size:9px;">
                            <span style="white-space:nowrap;">
                              <a href="tel:{phone}" target="_blank" style="font-family:Arial;text-decoration:unset;" rel="nofollow noreferrer">
                                <span style="line-height:120%;font-family:Arial;font-size:9px;color:#212121;white-space:nowrap;">{phone}</span>
                              </a>
                            </span>
                          </p>
                        </td>
                      </tr>
                      <tr>
                        <!-- Email -->
                        <td nowrap width="172" style="height:0;padding-top:4px;white-space:nowrap;width:172px;font-family:Arial;">
                          <p style="margin:1px;line-height:99%;font-size:9px;">
                            <span style="white-space:nowrap;">
                              <a href="mailto:{email}" target="_blank" style="font-family:Arial;text-decoration:unset;" rel="nofollow noreferrer">
                                <span style="line-height:120%;font-family:Arial;font-size:9px;color:#212121;white-space:nowrap;">{email}</span>
                              </a>
                            </span>
                          </p>
                        </td>
                      </tr>
                      <tr>
                        <!-- Website -->
                        <td nowrap width="145" style="height:0;padding-top:4px;white-space:nowrap;width:145px;font-family:Arial;">
                          <p style="margin:1px;line-height:99%;font-size:9px;">
                            <span style="white-space:nowrap;">
                              <a href="{website_url}" target="_blank" style="font-family:Arial;text-decoration:unset;" rel="nofollow noreferrer">
                                <span style="line-height:120%;font-family:Arial;font-size:9px;color:#212121;white-space:nowrap;">{website}</span>
                              </a>
                            </span>
                          </p>
                        </td>
                      </tr>
                      <tr>
                        <!-- Address -->
                        <td nowrap width="248" style="height:0;padding-top:4px;white-space:nowrap;width:248px;font-family:Arial;">
                          <p style="margin:1px;line-height:99%;font-size:9px;">
                            <span style="white-space:nowrap;">
                              <a href="{maps_url}" target="_blank" style="font-family:Arial;text-decoration:unset;" rel="nofollow noreferrer">
                                <span style="line-height:120%;font-family:Arial;font-size:9px;color:#212121;white-space:nowrap;">{address}</span>
                              </a>
                            </span>
                          </p>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</td></tr>
<tr><td style="font-family:'ws-id m57yJL0n';font-size:.01px;line-height:0;">&nbsp;</td></tr>
</table>
</div>
<!-- Tracking pixel image (optional, can be removed) -->
"""
