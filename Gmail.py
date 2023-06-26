import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendGmail(data:dict, credentials:dict):
    try:
        sender_email = credentials.get("sender")
        receiver_email = credentials.get("receiver")
        password = credentials.get("password")

        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Alert"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        
        html = """\
        <!DOCTYPE html>

<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">

<head>
	<title></title>
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
	<meta content="width=device-width, initial-scale=1.0" name="viewport" />
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<style>
		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			padding: 0;
		}

		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: inherit !important;
		}

		#MessageViewBody a {
			color: inherit;
			text-decoration: none;
		}

		p {
			line-height: inherit
		}

		.desktop_hide,
		.desktop_hide table {
			mso-hide: all;
			display: none;
			max-height: 0px;
			overflow: hidden;
		}

		.image_block img+div {
			display: none;
		}

		@media (max-width:520px) {
			.desktop_hide table.icons-inner {
				display: inline-block !important;
			}

			.icons-inner {
				text-align: center;
			}

			.icons-inner td {
				margin: 0 auto;
			}

			.row-content {
				width: 100% !important;
			}

			.mobile_hide {
				display: none;
			}

			.stack .column {
				width: 100%;
				display: block;
			}

			.mobile_hide {
				min-height: 0;
				max-height: 0;
				max-width: 0;
				overflow: hidden;
				font-size: 0px;
			}

			.desktop_hide,
			.desktop_hide table {
				display: table !important;
				max-height: none !important;
			}

			.row-3 .column-2 .block-1.paragraph_block td.pad>div,
			.row-3 .column-2 .block-2.paragraph_block td.pad>div {
				font-size: 12px !important;
			}

			.row-3 .column-2 .block-2.paragraph_block td.pad {
				padding: 5px 20px 10px !important;
			}

			.row-1 .column-1 .block-2.heading_block h1 {
				font-size: 18px !important;
			}

			.row-3 .column-2 .block-1.paragraph_block td.pad {
				padding: 10px 20px 0 !important;
			}

			.row-4 .column-1 .block-2.list_block ul {
				font-size: 9px !important;
				line-height: auto !important;
			}
		}
	</style>
</head>

<body style="background-color: #FFFFFF; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation"
		style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF;" width="100%">
		<tbody>
			<tr>
				<td>
					<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1"
						role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
						<tbody>
							<tr>
								<td>
									<table align="center" border="0" cellpadding="0" cellspacing="0"
										class="row-content stack" role="presentation"
										style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1ed760; color: #000000; border-radius: 0; width: 500px;"
										width="500">
										<tbody>
											<tr>
												<td class="column column-1"
													style="font-weight: 400; text-align: left; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="100%">
													<div class="spacer_block block-1"
														style="height:25px;line-height:25px;font-size:1px;"> </div>
													<table border="0" cellpadding="0" cellspacing="0"
														class="heading_block block-2" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad" style="width:100%;text-align:center;">
																<h1
																	style="margin: 0; color: #28282b; font-size: 23px; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: 700; letter-spacing: normal; margin-top: 0; margin-bottom: 0;">
																	<span class="tinyMce-placeholder">Anonymous Network
																		Detection</span>
																</h1>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-3"
														style="height:25px;line-height:25px;font-size:1px;"> </div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2"
						role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
						<tbody>
							<tr>
								<td>
									<table align="center" border="0" cellpadding="0" cellspacing="0"
										class="row-content stack" role="presentation"
										style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #191919; color: #000000; border-radius: 0; width: 500px;"
										width="500">
										<tbody>
											<tr>
												<td class="column column-1"
													style="font-weight: 400; text-align: left; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="100%">
													<div class="spacer_block block-1"
														style="height:15px;line-height:15px;font-size:1px;"> </div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3"
						role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
						<tbody>
							<tr>
								<td>
									<table align="center" border="0" cellpadding="0" cellspacing="0"
										class="row-content stack" role="presentation"
										style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #191919; color: #000000; border-radius: 0; width: 500px;"
										width="500">
										<tbody>
											<tr>
												<td class="column column-1"
													style="font-weight: 400; text-align: left; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="33.333333333333336%">
													<table border="0" cellpadding="0" cellspacing="0"
														class="image_block block-1" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad"
																style="width:100%;padding-right:0px;padding-left:0px;">
																<div align="center" class="alignment"
																	style="line-height:10px"><img src="https://drive.google.com/uc?export=view&id=1GqS7VN3kVmwkaVCwXhDxjoIVG4OAjB-K"
																		style="display: block; height: auto; border: 0; width: 100px; max-width: 100%;"
																		width="100" /></div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2"
													style="font-weight: 400; text-align: left; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="66.66666666666667%">
													<table border="0" cellpadding="0" cellspacing="0"
														class="paragraph_block block-1" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
														width="100%">
														<tr>
															<td class="pad"
																style="padding-top:10px;padding-right:10px;padding-left:10px;">
																<div
																	style="color:#ffffff;font-size:12px;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;font-weight:400;line-height:120%;text-align:left;direction:ltr;letter-spacing:0px;mso-line-height-alt:14.399999999999999px;">
																	<p style="margin: 0;">Drear User,</p>
																</div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="0" cellspacing="0"
														class="paragraph_block block-2" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
														width="100%">
														<tr>
															<td class="pad"
																style="padding-top:5px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
																<div
																	style="color:#ffffff;font-size:12px;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;font-weight:400;line-height:120%;text-align:justify;direction:ltr;letter-spacing:0px;mso-line-height-alt:14.399999999999999px;">
																	<p style="margin: 0;">This message is to inform you
																		that we have detected an unusual network
																		connection from your device. This may be due to
																		a number of factors, such as a change in your IP
																		address, a new device connecting to your
																		network, or a security breach.</p>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4"
						role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
						<tbody>
							<tr>
								<td>
									<table align="center" border="0" cellpadding="0" cellspacing="0"
										class="row-content stack" role="presentation"
										style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #191919; color: #000000; border-radius: 0; width: 500px;"
										width="500">
										<tbody>
											<tr>
												<td class="column column-1"
													style="font-weight: 400; text-align: left; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
													width="100%">
													<table border="0" cellpadding="10" cellspacing="0"
														class="divider_block block-1" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad">
																<div align="center" class="alignment">
																	<table border="0" cellpadding="0" cellspacing="0"
																		role="presentation"
																		style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
																		width="100%">
																		<tr>
																			<td class="divider_inner"
																				style="font-size: 1px; line-height: 1px; border-top: 1px solid #BBBBBB;">
																				<span> </span>
																			</td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<!--[if mso]><style>#list-r3c0m1 ul{margin: 0 !important; padding: 0 !important;} #list-r3c0m1 ul li{mso-special-format: bullet;}#list-r3c0m1 .levelOne li {margin-top: 0 !important;} #list-r3c0m1 .levelOne {margin-left: -20px !important;}#list-r3c0m1 .levelTwo li {margin-top: 0 !important;} #list-r3c0m1 .levelTwo {margin-left: 20px !important;}#list-r3c0m1 .levelThree li {margin-top: 0 !important;} #list-r3c0m1 .levelThree {margin-left: 60px !important;}#list-r3c0m1 .levelFour li {margin-top: 0 !important;} #list-r3c0m1 .levelFour {margin-left: 100px !important;}#list-r3c0m1 .levelFive li {margin-top: 0 !important;} #list-r3c0m1 .levelFive {margin-left: 140px !important;}</style><![endif]-->
													<table border="0" cellpadding="10" cellspacing="0"
														class="list_block block-2" id="list-r3c0m1" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
														width="100%">"""+f"""
														<tr>
															<td class="pad">
																<div class="levelOne" style="margin-left: 0;">
																	<ul class="leftList" start="1"
																		style="margin-top: 0; margin-bottom: 0; padding: 0; padding-left: 20px; font-weight: 400; text-align: left; color: #ffffff; font-size: 11px; font-family: Arial,'Helvetica Neue',Helvetica,sans-serif; line-height: 120%; direction: ltr; letter-spacing: 0; mso-line-height-alt: 13.2px; list-style-type: disc;">
																		<li style="margin-bottom: 0; text-align: left;">
																			WIFI Name                            {data.get("wifi_name")}
																		</li>
																		<li style="margin-bottom: 0; text-align: left;">
																			IP Address                           
																			 {data.get("ip_address")}</li>
																		<li style="margin-bottom: 0; text-align: left;">
																			MAC Address                       
																			{data.get("mac_address")}</li>
																		<li style="margin-bottom: 0; text-align: left;">
																			Internet Service Provider       {data.get("isp")}
																		</li>
																		<li style="margin-bottom: 0; text-align: left;">
																			Device Name                         {data.get("device_name")}
																	</ul>
																</div>
															</td>
														</tr>
													</table>
													<table border="0" cellpadding="20" cellspacing="0"
														class="button_block block-3" role="presentation"
														style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
														width="100%">
														<tr>
															<td class="pad">
																<div align="center" class="alignment">
																	<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" style="height:40px;width:102px;v-text-anchor:middle;" arcsize="10%" stroke="false" fillcolor="#1ed760"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#000000; font-family:Arial, sans-serif; font-size:15px"><![endif]-->
																	<div
																		style="text-decoration:none;display:inline-block;color:#000000;background-color:#1ed760;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:700;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size:15px;text-align:center;mso-border-alt:none;word-break:keep-all;">
																		<a href={data.get("map_url")}>
																			<span
																				style="padding-left:20px;padding-right:20px;font-size:15px;display:inline-block;letter-spacing:normal;"><span
																					dir="ltr"
																					style="word-break: break-word; line-height: 30px; color:#FFFFFF;">Location</span></span>
																		</a>
																	</div>
																	<!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
																</div>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-4"
														style="height:60px;line-height:60px;font-size:1px;"> </div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>

</body>

</html>
        """

        part = MIMEText(html, "html")
        msg.attach(part)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, msg.as_string()
            )
    except:
        pass

