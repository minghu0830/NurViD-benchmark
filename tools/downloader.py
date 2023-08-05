import yt_dlp
import json
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import os


def download_video(video_id, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, f'%(id)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'ignoreerrors': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_id])
        except:
            return video_id


def download_videos(video_ids, output_path):
    os.makedirs(output_path, exist_ok=True)
    failed_videos = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for video_id in video_ids:
            futures.append(executor.submit(download_video, video_id, output_path))
        for future in tqdm(futures, total=len(futures), desc='Downloading', unit='video'):
            result = future.result()
            if result:
                failed_videos.append(result)
                file_path = "failed_list.txt"
                write_list_to_file(file_path, failed_videos)
    return failed_videos


def write_list_to_file(file_path, input_list):
    try:
        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == '__main__':
    output_path = './dataset/original_video'
    video_ids = ['--Ly-qjodoI', '-0z1P7sw2qs', '-1mH9wYWd5w', '-2N0GEdJltw', '-aeuTQzxq6Y', '-BtEiJjukV4', '-C7K3i5Ea7s', '-DMEyIfWBV8',
                 '-EPJquqxJ1c', '-FdD0-zF_K4', '-fKaTT9nnlg', '-fvRejnoN3M', '-ged3dOpfK8', '-hiZ75P9iyM', '-JSu9M6Re4w', '-k2pgWCPmsc',
                 '-l635D0n-kk', '-MsywHWz1Z0', '-NoC1rkNgnU', '-qXC-IUT7Hk', '-QznLhQqdHI', '-SZbLkUKfAc', '-uyBJ0nv4oI', '-UZx2zSTfdo',
                 '-XBAxsIcQs8', '-Y2wMe48BfI', '-Yst1qShEbo', '-zlNQfbrStg', '-zT0oDRiz6E', '-_OkMf_umyE', '0-90-ucVHFs', '00ZWd_WwJ3g',
                 '01D17PnsGpA', '02PqJ8iPLxQ', '031fy7eHW4o', '06Eero7ok5A', '06wv8JmNyy8', '06XQuZLTENE', '07wJDVB95dI', '08eXvhJZprk',
                 '0a3B_9RNCPQ', '0B4x_mHgVN4', '0CCSV5QFgGo', '0cGHykGfO-U', '0dUlnBGu4rY', '0F62OyVKOwk', '0fJPgUFJLcQ', '0h9Bj-OLSr0',
                 '0IWzSE0ZSlE', '0LPkpY4KIkU', '0MIQLk4nwms', '0mSQn8SBmRE', '0Oj4AsZruZk', '0RcsKGEc-fw', '0t2t6Lh-k3U', '0tKSN4M_YZI',
                 '0VGuYnlB2Yc', '0vjVJuPik9k', '0vtVEtVXVz4', '0WMoZ_sInmc', '0xT5mfWrW_I', '0z5Xtb8ipRo', '0_qk_CrqRM4', '0_XPg6jBVvY',
                 '11hwCe3w_UU', '1bNc2CgwU-4', '1e7USvwCAxQ', '1f4VGwqUKYI', '1fV0Y5QLzLQ', '1jOmhNgJNuY', '1jw80-_vWtA', '1K7alb7Ne_A',
                 '1lsprM6MJ1A', '1mfjSry8WUQ', '1nDjNf8YXlE', '1OakmxZDa5c', '1OgR_bJM_Zw', '1Onm7fJ0zYE', '1PNlj_VEDtI', '1PqD-MYDV3g',
                 '1rlxKsx_n-Y', '1sje0zq-F10', '1WLcyNiBt2s', '1WxoWefo7gQ', '1_2u8oNloBs', '21v_YbzDiJ8', '23Ioifx2zX0', '24Jlbd9bOr4',
                 '25DJ1kvaN60', '25efi9K5eOQ', '29QOClzPHGQ', '29wOwkW7-ME', '2hAmWBEzFBU', '2i_rjQ9SGa0', '2KtmwJDhujU', '2M2gPCNunZw',
                 '2oztxG2wEVU', '2paEgKKEK5o', '2R2CzkzVdL0', '2rZoIVf4pYY', '2sNV9dixX4o', '2SqBXs-Y3ts', '2tjFVGih71A', '2Ux_m8iCgcU',
                 '2vt973I9_1Q', '2WsBzx82CnQ', '2ZvWaLst-E8', '2_-EBIujCQw', '3-SOKCuMujc', '31lF8VNCJ8k', '31qBW0Imj_0', '31rEOB9AwG4',
                 '32zHF9Yvyp0', '34TOon0KiPQ', '396l_q4T1NA', '3cUkDXZzeyg', '3dTzfSRxRZc', '3fk_8uR_uhQ', '3gLhooOemZw', '3GO_A7O8ILg',
                 '3iQ664gFHLw', '3kXnL0AQhYA', '3lorXZWgnDI', '3MeO7o0m7oU', '3Nw_fZ3B1sc', '3OjroDjmskM', '3RCUz_d9XQQ', '3Vlt_EZRGgc',
                 '3yA1e4RFlfg', '3_UUq7p6-5M', '40ad0Iq23KA', '40bZthiD2o0', '41y1unGur-Q', '44mJ9VUsGHM', '45C8N8mRKcc', '47dMHoWKpWI',
                 '47FjtSgpN4U', '47UgIBUoR_A', '48M_CwJE7Z0', '49jF6RZy3GE', '4A2I-sZHXvI', '4B_rg5uTRIo', '4c6bm_iT6pg', '4Du0_Sd_s2s',
                 '4eHQ5KmOZaM', '4eJAxp-gqn4', '4fQUQ94fPYM', '4GpXy_srgRs', '4MVIhgbTOsk', '4NAJuycN4Co', '4ntqS_R1r70', '4ONAC6uE6xA',
                 '4Qil5I1XLZ8', '4rifH8nB48o', '4rQkQj3gv3Q', '4UdYawfe1R0', '4UvjeoJGgV4', '4yQO__Khl5U', '4zxgX9IpmMY', '5-F_W5WYLKI',
                 '51ecxm8oLP8', '57I72z9R1H0', '57zApLuswoo', '58Ku24EerKw', '58wAvY_aF-Y', '59B4LwCURJ0', '5Cid7q9_Uq0', '5DSG23B5XGQ',
                 '5egAHIPiGlY', '5EVZHPaszAI', '5FfVjiou_YE', '5Fud4xTBgwk', '5FUnepktYxE', '5I1lclB_tPU', '5jci72lIJ-8', '5KPMeBTNOfA',
                 '5nQYrFwC7G4', '5q4APWu8FDY', '5qd1EONfJi4', '5qfIRPxoHuw', '5SJxq-D6-Bk', '5W3o4HjyV2k', '5w6EUzNYLXk', '5wxGEfY9egw',
                 '5Z-teZy3bCw', '6-33XEnm3to', '64-2Ly9aBn8', '660fOrTJnCc', '671uYTHpalI', '69VYrk0GeaU', '6Ayxz5p7GBs', '6BnxXcUxcBs',
                 '6cSbLJnjzTA', '6DCKEQVAFR8', '6eGGq4fz8SE', '6Er52I7LxPs', '6eY9QGkbmlU', '6gc07xlcuWU', '6jbVcMgN_HI', '6n--CYH4Pw4',
                 '6Ny4wSUdYNo', '6oHYb6_bFYo', '6s27NmJQi70', '6Xu2Sgk1y80', '6Y4DDmlWtwo', '6ydbP1_C8rk', '6zcsYUqaWCE', '6ZX6F1PUUe0',
                 '71LlfdW548U', '724-cEL_Z6I', '74kVE4Ixn8g', '74ttY4-QlIE', '77XNYG1twd4', '7Bm_BwZrq6c', '7CTdDHBzj7Q', '7F4nYxJgoJY',
                 '7jRryPp8C3A', '7kv3YZNpo8Q', '7l7hZVYkgto', '7OGnuOkTDsU', '7Ps9jswWgbw', '7q6HHVy-bjw', '7qYYDH4NUj0', '7s8W4dnsFQQ',
                 '7XPQYY0B7Rk', '7XyfHY9iSWY', '7yDymtT809s', '86RzAgHu75U', '87mdfPOh_Rw', '8Ab1Z-c3EjU', '8BaeLRCb0B4', '8CGlrISSmnU',
                 '8j0fucgtSGM', '8MPdw-0HbTg', '8OTKidNwLlo', '8oX4SQHxKBw', '8PKKTwzxG7k', '8pKp9dnRX7c', '8PZqdLjy5Tc', '8uXhDt79KNQ',
                 '8vKssX6wvwY', '8w-3h50E17Q', '8WEjKytxNxg', '8WU3Q0_dYXY', '8z44ryOVEEM', '8_LRJ8vLMxI', '95lKeVet2qQ', '968cu9kFRPM',
                 '98ftIyS59lw', '99TlXo46g0I', '9akxlH6BtyM', '9ba1LjgPHGg', '9c1Jq7Ekago', '9Dgjirf3Dss', '9FvUsjje8ic', '9i2oJR_1ZXs',
                 '9jAc3y6Gv4k', '9JLVK138A4U', '9kOYDulwQv0', '9LYBiLy_a-k', '9mGUSQKOVw4', '9MMc5A0MMWg', '9msWAqfA5lg', '9OCVSsKJsdE',
                 '9oeVA0nl0m0', '9r1ShyTIJ90', '9rDS5VK1Xqs', '9sFPahcX7z0', '9umaLJ6qdXo', '9vhOSbxGle8', '9VHtLRhwrBM', '9VKox-wy4fU',
                 '9XkOssKciqU', 'a0RhbpehcQg', 'a1-dLLOeKUA', 'a1DFmgLJmMk', 'a4L_014Czao', 'abNuOlCTu-g', 'Adcba-WMbEE', 'AdkoFiFrz7o',
                 'AdnKbipn5es', 'ae1lL3GLVdM', 'Af4CT12J8GI', 'afFMH2lgH-U', 'ag5-goiMNsQ', 'AGnKuYiN1Bg', 'AgVZ3p8OJ0A', 'Ai3YQJbuS0A',
                 'AI8jESrzqx0', 'ajDGW_bOm5Y', 'AkeRnPUGdv0', 'aKPL2Rmj0hI', 'aKTGjx3afvs', 'aLoP1MG8aLA', 'AMO52zk3AXk', 'aN78RVfe0Js',
                 'aNc7TR80tVo', 'ANVFQV0PHIo', 'AnYWNPDKwjc', 'ap1qFh-lS-8', 'apJZq1vEjLQ', 'APQwu9Qx3As', 'ApSPE69IPNc', 'aq8OwFaIQ4I',
                 'AqBOMERKS_4', 'aQYQtmzkd28', 'aR73Ik_GthM', 'arqG_2ftfOY', 'ARRfrFwC87M', 'AuGRfsWTFnA', 'aUkEBsZGfA4', 'aV9JJSTU6Ak',
                 'AvbxofLe-MI', 'aw_2mvb69Ow', 'ayf3coj_zMQ', 'aZ3DJnCxujA', 'aZOYJigvPbI', 'azQ7tuTFmno', 'B-g_5WLffMM', 'B02i_pL7CnA',
                 'b1nxS_yjiEk', 'B1oCcX1BCrQ', 'b1uy8cwYlcM', 'b26uL9PtfKE', 'b2UCiQs0KMg', 'b6c4-U6Z1RI', 'B7SJ3QW5nik', 'B7SWLiDjMvI',
                 'b7WIr_JkgLQ', 'B9LzzcN3JmE', 'Ba55wzNxM2w', 'BADeHh0xNME', 'bctTKygOj6o', 'bE4MZ6NQhsA', 'BfP1yZevi1c', 'bFrFHy_JEDk',
                 'BfYvfy97D0Y', 'bGRpVOlkmSI', 'BH9mYVQGdm4', 'BHH_nHIhJO4', 'bj1LoKDgR4A', 'BJ76KUwrn3I', 'bJ7ilV9872k', 'BJXsXISIQhk',
                 'bL3PQ_3hrbc', 'BLm4fCyj1CY', 'BloOJGSZ2S8', 'BLoV1TTTe9Y', 'BLVruFeiJGA', 'BM8hJsBsRXI', 'bmI0TI0M9D4', 'bNLtwX2LDQI',
                 'bnMRJzhF2lI', 'bnvs8IzCQqk', 'Bpng0Ex9pho', 'BQHKdSKK7kk', 'bRPSi32Gcw4', 'BTBBzcdZ0kg', 'bVbBCtiFIPU', 'BwJL9FO6fMg',
                 'BWph-kU5VcM', 'BwzeCSd2bVc', 'BxhVnMPLR2I', 'BXWkN_YAMnA', 'bZWr4lidwaM', 'C-tFDOR--fQ', 'C4uRBT4IxWk', 'C5lVMsrp33E',
                 'C5PgxwxA9XU', 'C7r2LlGqrcE', 'Ca-nhIeZxuo', 'casR8s0oS6g', 'cbltQ7-EZJ0', 'cbT18UtpGJQ', 'CbwhqSnt54I', 'cCgdYZoybhY',
                 'cctNcVuGYfo', 'cCzwH7d4Ags', 'cDcuU3KVpuo', 'CEq6QWOHTlo', 'cEWXs-UmOuA', 'cF1Nu3o87Z0', 'CfEymG-VQNQ', 'CgNZLuHrV0o',
                 'Cgrn1Vr010E', 'CguNhVWqojs', 'cHPUPBFVHaU', 'CIBf9EewvU0', 'cIx7mOV8FM8', 'CJrrnLxe3lc', 'CJ_-t9AtkpA', 'cK5YxQFFlZE',
                 'cKtB81VN_4Q', 'Cl-Cn0qK5lg', 'ClWyk7-Idq4', 'cM1H92_5hqs', 'cmUXo4Crrm0', 'CNjDXnLcVfA', 'cnp4XfHaQgE', 'CosdRXJ9jAw',
                 'cpnRZgCWIXU', 'Cpoc5ht51NY', 'cqD-EvrqhKU', 'cQm4r5QFHBA', 'crCCyOlDY3w', 'crSd9cVn0qo', 'cTSUeeG12Sk', 'cTVnjY0bXlU',
                 'cTwCK3dRV90', 'CUT22MsW04I', 'CWEIWlqueBY', 'cWyPbYD9lGo', 'cx5G1VdC9UA', 'CyczQoe3MiQ', 'CYiHiRd6l1g', 'cYzF4GOE8Fo',
                 'CztDIt5nen8', 'cZ_eoeZx6kY', 'd-SGsAN22lU', 'D3s7heDD5rE', 'D47KVB-oT98', 'd4EOOvtqj6Y', 'd6JZXKg79yA', 'D7FnXaoPwR0',
                 'd7ymmR8WuYE', 'd97m4pNuBEI', 'dAF1K6DR8i0', 'DALragCYQr8', 'DbDBriTlmms', 'Dbl84rzEZWw', 'DBulVOm5LGk', 'DbUNhWmKw4M',
                 'dCyakRWH9a0', 'DFAHKL_l6KE', 'dFebX7PCg3w', 'dGV5XWzPF9Y', 'DhfyYXvszBU', 'DhGuOzl5Aks', 'DhlIQskLhKU', 'DJd02xCNNc0',
                 'djiMq2c_fCo', 'DKXMxzegPAE', 'dl-p2Kb44B8', 'DlENkC5Zwg4', 'DMh25N3Qa4Y', 'DN4E4VunBAo', 'DNAtW0EVR9w', 'Dngvez7MLiM',
                 'Doqwn0_xe8I', 'DPbxUe4qyyE', 'DQRPCEbGFSk', 'dS9H3EMxQJI', 'DscPAFMdo1w', 'dSPO1KBwUXo', 'dtL-2hf6RHk', 'DuO1tWIDEe8',
                 'dWE2jGv8-8E', 'Dwj4qZcN2Cg', 'DxA2Nng_KBo', 'Dxb-zo3lWPM', 'DyHsx_AOrzI', 'Dy_OnvkVG5Q', 'DzDDgK_PdR4', 'DZVoNuBsjN8',
                 'E3lxXZHSkdA', 'e49kAYjvMcQ', 'e595abxh9m4', 'e61ASYkJIRw', 'E844Aa1b5hg', 'EAjzt1M4ueU', 'eaSp-INcrwk', 'EAWVQWpgvUA',
                 'eckl2DvLZIQ', 'EcvnyTIs9JI', 'EDdzJnJyIdM', 'edjwF_XlNzE', 'eDLHAN6u2yQ', 'Edz9o56EgD0', 'eEyTzVbpG3w', 'EF84272YoPE',
                 'efIdLoYdxps', 'EgFSMM3ReE4', 'ehAp300c0e8', 'ehnhb5_IPdI', 'eHw1ICKt8sE', 'EIhCVahxZkA', 'eIqBFOX5YTo', 'EJ4_zTzzNbY',
                 'EJD6BT-zPHU', 'EkcmabUBzyc', 'EkKtFMKRIXM', 'ELWyxjy4jOo', 'enDCSfO4GRo', 'eORbJowLOFg', 'eOsY84oYqKg', 'eqX2nymZHWA',
                 'eQzsy3NCFEs', 'erabEK1fB_c', 'eR_xGQH1qYk', 'et4GjVERUR4', 'eUS8tJfDV6c', 'Euws_PLlpMo', 'Evp5EETgGhI', 'ex90Nui_S5k',
                 'eylbjkgzFVk', 'Ez-dyu4gJEg', 'E_IXck9171A', 'F-VPXPctDV0', 'F0863luTyfA', 'F0ve4k_sINQ', 'f2oyLPHXNT8', 'F5MRDLajCz0',
                 'f6HtqolhKqo', 'f6N38hfD4o4', 'F88btEbzdw0', 'F98AtFqq2q4', 'fb29LCjX4-E', 'fBIrnLxKB94', 'FbTEEN7p-p4', 'Fd8GDFzySQ8',
                 'feVH2esO1FI', 'fGsYDa3bzzI', 'FifaSTgtaBU', 'fIiMJ80KVy0', 'fJBcBEBcKKg', 'fjcQKVFvPlQ', 'FjHtL7gIQLk', 'Fk2Dj6wyQAE',
                 'fkBuY4iMK7E', 'Fkev7W8rr3I', 'fkIeURclwn0', 'FkyW7DoWHAM', 'FKZDX79-fxo', 'fM0rd3yFSjg', 'FMmoEUEiFVY', 'fnBA9l-3liw',
                 'fnIPcKKj7gk', 'fnXB1xyRFaA', 'fOeg8IofzV0', 'FplYx3s8uEg', 'FQ5N13TlXLQ', 'FQJmw7b-ylI', 'Fs5P2Ptz3Vg', 'FSTfAqQpsrI',
                 'fu6kGcDpPWU', 'fwvVdw3tzg0', 'fY7SAR5RXbY', 'fyDyN2PRNGU', 'FyHooK1u3pg', 'fZ3RyWrtjYM', 'G-RjMWCE3U4', 'g-z44AlcZJY',
                 'G1EOqEUyDEk', 'g5vdCoCp4IY', 'G69MHKMNzFY', 'g9F8cTZ4eDQ', 'GASkp3nW4ZI', 'gatJCfnz6bw', 'gbAYUh77P7k', 'GbeLVnVmxX4',
                 'gBEtcBmZsp8', 'gbI3qxMQ5GE', 'gdJv2MwaDyc', 'Gds4pc2E8cw', 'GE24mrcUkhg', 'gF6EgRxF-xU', 'Gf9B_X02XWA', 'gfJozntAqZo',
                 'gFSf0fO0Lug', 'GhqVaxDZZ1c', 'GI9S9xdR5KI', 'GicBmU8bEIs', 'Gj8z6bFOU24', 'gJDGLzKcqyU', 'GmUrNFGqTA0', 'gmWjVoc3mM8',
                 'GnoMoLePRvE', 'gNuqWwOeG5g', 'GOli8l0nco4', 'gpS8AHh3dRE', 'GQbJ495g0nI', 'GrJWPityMfc', 'grtEi24r2b8', 'GSM9EYqf93A',
                 'GsypMFw4OJk', 'gt6PsX4upCU', 'GtX9CV7-EIU', 'gTxix8KzjkQ', 'gUWJ-6nL5-8', 'GWARv4-pNPc', 'GWBrbvIhncw', 'GWVtHjR5Psw',
                 'gYM6F3Yyzs0', 'g_1YRGKtQkU', 'G_TDLaTop6U', 'H0EtSorwGnU', 'h1L4gag4xnE', 'h7J28x6fRaQ', 'h8CtsPAaa5Y', 'hA52-4LDYng',
                 'hAoVAxErpsE', 'hCbdqjnstXE', 'hcPB2R1o0T0', 'HC_5oej-NWQ', 'HdXcdcyZwfE', 'heTQcEMDSGU', 'hGAZXMj_3gw', 'hhl8qC8wf3M',
                 'HJh3Sro1e44', 'hjMuvERM3aY', 'HjXMlsoLm58', 'HkeNWHeizbg', 'HknJP1qf-_0', 'hL6nWluFOwk', 'hmCduOw52N4', 'HnOMCQ-8Bfo',
                 'HnYm7y7jsMY', 'hOc3uL4alwI', 'hOOj_Atm_QU', 'Hp4WOXFIUvc', 'Hr01KkJvKYA', 'hR6sH_NSAfs', 'Hu0d8BfRpYo', 'HU7ZXAmL8vo',
                 'Hu8wMXKpQcM', 'hVwmifJdlfg', 'HWOadHxYUgA', 'HWrr0tJTlsE', 'HXI1V2VEkSA', 'HxT7E14euZ8', 'hxxXvsrIL18', 'hYXYcOHT6aE',
                 'HZEx6iNVDpw', 'I-y9hYJVHc0', 'I0TjUM8qYVs', 'i4qwUWVR0ik', 'I4U5qBSdUb0', 'I5qc5frLypE', 'i9InFg2vGf8', 'I9SR2wleAwk',
                 'i9VGEtH__zU', 'IcAIaBzQrkI', 'IccSohdKw5o', 'idL717ww3jE', 'ieTSyTRlyLY', 'If8ewVG8UZg', 'IFHriQpQB50', 'IfNLtevR64c',
                 'IhlG2J2PAbs', 'IiB3ZV3FHdQ', 'IIeq4I3pwHA', 'iIo5LtWfxrY', 'IisgnbMfKvI', 'IiueXfhu4D0', 'iivqpZsN76M', 'iiy9xPuVvYs',
                 'ijuoM54oCao', 'iJvKxxn40zE', 'IKjNOP0W76I', 'Il0iJUNnq7k', 'ilbYTM2tnpE', 'Inf44ssPIUA', 'InngTKk9zJg', 'iONubn3sC98',
                 'ipliu022a3k', 'iQCLPg5f3tE', 'irDLHivG1ro', 'IrhtHZFRBqU', 'IRwKri1rqpU', 'IwJlXwISDsI', 'iwvnA_b9Q8Y', 'Iw_sNY02eh4',
                 'Ixzc6RJv3GM', 'iyVphDMrJ9M', 'IZORhyAHhZs', 'J-8WcSqVwq0', 'J0KI-i6aEmc', 'j2iuJUSaUT0', 'j2VfzKjn4no', 'j4vCio2bdbo',
                 'j5dwnDyxh4E', 'j5GYMOvjjtk', 'j7bdt74NOcQ', 'J8dkqhWBWTA', 'j8s1B4ew7U8', 'J9L26AxMLEw', 'J9V8oVSIqXI', 'jaAehsIKB40',
                 'jc9LampMMU8', 'jdL_GmE84Pw', 'jDRvxKq8JzU', 'JEiHJoC6ChY', 'JEPqvTVdqVc', 'JF-pIZsJvZQ', 'JGgzTJtzaqc', 'jGJNtSF2RLA',
                 'JGOFzgtKvXM', 'JjETsqPoCzA', 'JK5rb6acQvY', 'jkhFGLGxnrQ', 'jKR8SwI0gFw', 'JLkujIaDKsQ', 'jmkX612KfQE', 'Jn8QxcBTI20',
                 'JNoEDzEMzYw', 'jnTdshj2r4g', 'JoGYWfM7UG0', 'JpGuSxDQ8js', 'JphvDiE09UA', 'jQkZvGXgNDs', 'jt7SYhALtPk', 'jU4PVlIKvlY',
                 'jusD8raVyT4', 'JvMFjGjnBJc', 'Jwo92kqtUTg', 'JwSSrQzw5FM', 'jX6rIhIXu1k', 'jx7SAKhFhHc', 'jXLIvgWNW1A', 'jyGj_vBpM6k',
                 'j_cMKkyp6q8', 'k0RbwgZbSAg', 'K4rGww6FGMg', 'k7pxeGS1a3U', 'K9cYoQ1BScI', 'kaJv3ap5y2g', 'KBDLtoPR140', 'Kcih9VWhp98',
                 'kCJWzRrD71M', 'KCkXJZP9MNw', 'kC_97FdzxUY', 'KdPIAgInIGU', 'kF3_Y3LOM0o', 'kfSEV8o6-wY', 'kFtMQc70MS0', 'kGlSXbnNYvI',
                 'khKKkn-7vQM', 'Ki388Otp0U8', 'KIDsL-6Y2G8', 'KImmBXpM7js', 'kJnHKsvBjho', 'kjYJfpQ1v5k', 'kKgJMY8QFis', 'kLKJF1yy4T8',
                 'KlRTtDJbyxQ', 'KlWqFDhEphc', 'KMdkwYGpONo', 'KMJCl5PU7yo', 'knuKaVRdR5k', 'Ko-oArJLfFc', 'koYdj0vemwQ', 'KPRlLx6-WKg',
                 'kpvuGfHEz90', 'KQNaB37x8-A', 'kRaVPCzsbyA', 'KrcBZCqx37k', 'kRDMBQEL4I0', 'ks5NHqYF6kQ', 'kSHJ27s6Jsk', 'kUXumDhW_tc',
                 'kvcX078gIS8', 'kvfiB4a5AHg', 'KVKop8m7oUU', 'kVMfKVJN5J0', 'KvNo4ITlaDw', 'kX4D3LLDvIk', 'Kxb43B7iWFM', 'KYo2YXlJjKg',
                 'kZ6i3JSqE8w', 'K_ituJgAv98', 'K_Yv4ahcghI', 'l-CWyxBYfv0', 'l-Nlm55ztEs', 'l0nNt6GOEMM', 'L2AQMNL0Oow', 'L2cbtyuqRXE',
                 'l2svlMYCBiQ', 'L2vZDVY0Wro', 'L4LSRgdie-c', 'l55OSJl6hIk', 'L8j9F0zm-4A', 'lA9xa01b-Ds', 'lB1-Rmlr4hg', 'LcaiMHduqPc',
                 'LcVrAL3yFC4', 'LdhWCPdV0T8', 'Lfe8MgI8eTw', 'lgdj4hOEYuM', 'Lgjy-w7uv7o', 'LGYxwWtJWLg', 'LhMRLPkxRu0', 'li4m2dCN7bI',
                 'LiSDivNECTs', 'ljJnlOOAkXQ', 'ljSkvtnTlIo', 'lk6GYVM7enk', 'LlGYef6PhGw', 'lMTI6MtL1wU', 'lmzLNpyDnF4', 'lNnvx6hIN78',
                 'Lojv2N_bz_M', 'lowOxcK5JAA', 'LPKSw4VUhew', 'lPWGq3p9KdU', 'lS1PN8Fdd4Y', 'LstlIyTlT3k', 'Lta0GbIKCZA', 'LTFWGGL859w',
                 'LTudru2FF9I', 'LUDic-RyUT8', 'Luru8cYPFY4', 'LyWtN-oRjN0', 'lZ-vwkNg2ho', 'Lz3gtI1fDdk', 'lz3JDsDHmxA', 'lzmn9_OdR7A',
                 'l_Vk83J_TPI', 'm0xTVy6djRE', 'm0yFpcqKAm4', 'm1cKMlY7Ovk', 'm4VCmdKJgtY', 'M66jTwPBL9Q', 'M7ZMSsUm2pM', 'MAikOv859sY',
                 'MCpife5sFPA', 'mCQCLkAcn0Y', 'mDqdX0fDb24', 'MEbsVeGnqJo', 'mekhnm2-NZY', 'mEZ3hxK4WEM', 'mfiWikreG4k', 'mFURUnD8eJs',
                 'Mg5efWa7I6s', 'mg7Esx3UXUc', 'mHeETNVXeoY', 'MiDnGwVBUz8', 'MkvKYP9vLsE', 'mLbySoiCuyo', 'mMcz8jeAvIY', 'MmnY2RtgCZE',
                 'MMuDoHHZyhI', 'Mn-iKqxvUyk', 'moqWBk6Ulfc', 'Mq4Yh0-iozY', 'mrRVEiyEO6M', 'ms1ZwHe-g3A', 'msPBI-LVJ1o', 'msRft-g-k_s',
                 'msUTYi295qQ', 'MT9_FjukU4w', 'mtgdUp17Zx0', 'mtpVrWkO8iE', 'MTuDsaPbEEk', 'mXaFmSQmC8E', 'mXn3f-o-l_M', 'MYaFQFiVz4I',
                 'mYr92slTr0k', 'mzkLYjDznPw', 'm_RWZGoHczY', 'N18GtJ7znh8', 'n3Ed36YSz9w', 'n4xISnZRmkY', 'N6aqYkq0xlQ', 'n6gD9nl5_vk',
                 'n6l19CWi710', 'NAleiCTByWc', 'nany227g7to', 'NBPUBLied0o', 'nBT7PfC6YB4', 'NC-Lult6iM8', 'Nc2zl2SeQNo', 'nDo7JJHvve4',
                 'nf-WaUkzTGc', 'Nf1mw11UHAg', 'nf4oCSeAwBA', 'NFYqYfzB9bQ', 'NG7E1OKqpIk', 'ngYVqyOeqe4', 'NJib85nKy5k', 'NJJbE1ZaPOc',
                 'nkBTikaXrck', 'NL33d3ivsnI', 'NM53mj1iQBo', 'NmoERV9EmG0', 'nopgqBoUmYg', 'NP0ybURoSz4', 'Np90zUnCB-g', 'NPDxtgCLBmY',
                 'NRp7xXLpyjc', 'nrw1s_Z47O0', 'Nr_VTtWkNHg', 'nS00pPC1NZE', 'Nsm3HIH7QdU', 'NttqBWSA_DM', 'NU-J9jkNp8Q', 'nUjRM_ya1m4',
                 'Nv8tTPsiFCA', 'Nvrlfmg8QkY', 'Nw2bLljtueg', 'nW35FpRBOFE', 'NxHCozu-sBM', 'nxhI2Vg4xHE', 'nypJl5OQ34g', 'Nyqr7_JmBok',
                 'nZ5ARMIiQ4A', 'nZxbfboIRvU', 'N_31dk2VumQ', 'n_D0Gt2pL-0', 'o-_ku8TTVQM', 'o0zEmaGBgBY', 'O1H0HGnmar4', 'O3StYjvfjUo',
                 'O6W7r7PzjMA', 'o79esR_TQxk', 'OAHG5xAeuZQ', 'oakADmlMc1c', 'OANJbkMy_Ss', 'oaOOXc9QLwU', 'oAV7ZzoYNss', 'Ob6TYXo6CxI',
                 'obdMG9wwcPE', 'Obloj84_72k', 'OBVqxwggZ3U', 'Oby_tVxQZAI', 'OdDDaVpHojg', 'ODfGbQ-qsak', 'ODmwCavm6kc', 'OEWTy2FUIiA',
                 'oFzfGZOYCDc', 'OGezrQzRN58', 'OGhQITOzX_c', 'oH7SorAES80', 'OhShkKHk9-M', 'oJ8cE0-xGF0', 'ok1TeEEBonk', 'OkZeVDj3WI8',
                 'onfb5EX23bo', 'ONRQrqxZ5kY', 'OOALW5_5AOw', 'oPH-8S-d9Dw', 'OqSDh--PZig', 'OQYI20QZhRg', 'orcK0EeVkgo', 'oRSDFuBCia0',
                 'OsVL10kIh8w', 'oT-6ZF1r1fw', 'Ov-BBUhKdJU', 'ovxMconfxRo', 'OwhjTacbn_I', 'oWjA-D0ugg8', 'OWK9Ut3PA1k', 'oxdaSeq4EVU',
                 'OxlsLZcvRi0', 'OyBYv-PAGzU', 'oyIb_WQJU80', 'oYUa-BtQnvE', 'OY_W2-ZtPRU', 'ozg-_3UPmoQ', 'O_0pglA201U', 'O_c6g8fAMxs',
                 'o_qXg8h3J9Q', 'p0l9ONq9Rsk', 'p0ydXpe9QDI', 'p2h-6KERCyw', 'p3yBBNM3l4Y', 'P4JOSZbfrGM', 'P6sfE4T9FvM', 'p85kCsduF8M',
                 'P8s4vpliKs4', 'pae-MY3-1xw', 'pAJmtKqoKJc', 'PAMMlaYVIZo', 'Pb3S-FuBwIM', 'PBeKnXxiblQ', 'pbmC27Z3kuc', 'PDbkTqHgziA',
                 'pDBQ_N-6rRE', 'PeEVL3aB-T0', 'PEuYlcxUuHw', 'Peyw-eKZJOI', 'pF5MJIw9pt4', 'PFJBPXsMMKE', 'pg-xeL-4nyA', 'PIBP3lEJCKA',
                 'pIMX96z-eWQ', 'PiZbnalFlww', 'PJcwc0GB0Is', 'PJO4dgqCs1g', 'pJrLxSVI-_A', 'pjz-IdyTNTU', 'pk9ZB9jovGQ', 'pkn4hYvcaD0',
                 'pK_7NE5_yCU', 'PLk3Yfj3lM8', 'PLSOON6Vf9Q', 'Plu2rBU_Snc', 'PmhpqrIBJD8', 'pmpscqwoQpA', 'pN1tZo4eaOM', 'pnxRN_Yuyss',
                 'poKa9lU4Pxs', 'Pp4t7K86S7k', 'Pp96EhX__kE', 'PPm23MshGio', 'PqB19w4v_fc', 'pqdT_9ZHkcA', 'pqrT_abh-EM', 'PRFGSwr7-Po',
                 'prHuJ_74iZc', 'PrwADKcE-ts', 'PVgowwPth5M', 'PvhEjE0Z3tk', 'PWMIqJRXx0Q', 'Px-JGoUNN6U', 'PxB8kSbydPc', 'pXCTmVOT82s',
                 'pXJDcHhQ_QE', 'PXquGIXXk4s', 'pz7aYDVWRX4', 'P_EK5c4T-nU', 'q-Ax4tMtBYY', 'Q3a3w3GtbJQ', 'q6Bsqqo0hNE', 'Q6x0omrhsoo',
                 'Q8lZR3Fo6SM', 'Q9daM1wqPxs', 'Qa7I1xf6eKE', 'QANmjYtiA0Q', 'QbCDXXlGDdI', 'QbGUPetvj84', 'QbpJ5QUZXIk', 'QcxSQ6VaqfY',
                 'Qdha875hRYs', 'qeZDy8O_cn4', 'QeZF3chcmIk', 'QF8lOgjCKEs', 'qfSFx93S5cY', 'qfXX37b-Df0', 'Qg-ouP03qLs', 'qiuQaa1F5j0',
                 'QizxF-7AVRQ', 'QjlSrL6ZfhU', 'qJMX7TPq48o', 'QllyroV4kIU', 'qm7nAdh63ao', 'qM_GS8Swk-k', 'qoaSvUkPDWk', 'qOjWJHdEaBo',
                 'qOM9ia17Nwo', 'QOv1rGr2-0g', 'Qp78x7NxUho', 'QPIJPAQNx-o', 'QQIRLu-XoIE', 'qRmUOlCgigg', 'Qs6P8vv0R_c', 'QSnEA3OMJl8',
                 'QtctitWArm0', 'QtCYebM3f8g', 'QTz9BM4vYtk', 'quqV86VI6Ts', 'quwzg7Vixsw', 'qvK05MslzKA', 'Qw6I97mDOKs', 'qX7qRYKxN4g',
                 'QxBEYqYpkMk', 'qXKQQmCgKG4', 'qXOySyYARRg', 'qXtsl5_G7wM', 'qZ3Q9p-7WCA', 'qzaPWudLatE', 'qZpmrTBIiD0', 'qzZD-XzxIMw',
                 'r0azePlFx5c', 'r0boh-NbFYY', 'R0vlehzbAGE', 'R1hxfEuYlbM', 'R1usywaxSdU', 'r2ZnKUawEsM', 'R35AdZxATJc', 'R3Fx9G0r5iY',
                 'R5Fa6n4cnE4', 'R5jd4SDEcsA', 'R5JTKMWCzQ0', 'r8okzAL6PlQ', 'r9tBp-sKMbU', 'raiufF7FuQg', 'RauG9bE3klg', 'rBD71jLxg7o',
                 'RBPpgeKz31s', 'RCfmV_oW-Jc', 'rDtZWq6jgYw', 'rE2VFknFfwQ', 're6TnoGpXdM', 'rfCpegI5fHE', 'rFF2z5nnW2Y', 'RFFBfBdScxg',
                 'rfRjmz5DvLw', 'RG7mBpT4Rw4', 'RH-gsrUwLrA', 'rh02673jFEI', 'rh0vqINBrpM', 'rHt_bX0MfQ8', 'rIdTJv_wT0g', 'rISS-nR_Ug4',
                 'RJQ5Q5jQZmg', 'RKDO3pfICjs', 'rLs-Ta6h6zU', 'RmeY9KQQ0qk', 'rmht42iboYQ', 'rMMpeLLgdgY', 'rNnEiYVU6lg', 'rOc1enHcEh8',
                 'rOH2qF3EtKA', 'ROzfJO6Fkcs', 'RpB_qVyrIgU', 'rPTLcEBI5Fc', 'RqhoTKnV-zI', 'rQrJzKCPn7E', 'Rr1RuuVML6U', 'rrUC9449bp8',
                 'RSpxA3MwdVc', 'ruhNNUsD4jk', 'rV1rttrlA08', 'rXHfRWQ42xo', 'Rxtg5eTnICM', 'ryY29F8Wx_I', 'RzpVnqPwfhs', 's1NiJOmyaLI',
                 'S1ThWb94XwM', 'S2TzVzgRyLY', 'S3uPFcU4qRo', 'S4jQzg8GrXY', 'S4L6rVLMQ0Q', 'S648xZDK7b0', 's89pcR9TzFc', 'S8H95BfLg-4',
                 's8V5IUK38Xs', 'sAkzifd81rk', 'SbYke2NHhRs', 'sC9vpZLLLLI', 'SC9vvK7ZaTQ', 'SCF6bmk8KWc', 'SClSnPYIay0', 'SCvBusvxTnM',
                 'SDFjrkfSjDM', 'SDl6psYRA_0', 'sFFxRTwbhNY', 'sfOm5TBAFVE', 'sFsibuhZ3oM', 'sGfQqniqV9M', 'sgiGXaeT-EU', 'sgtYQbNfURI',
                 'Sh000UgtLiM', 'ShRI1L0Q0gw', 'SHx_P08m3_Y', 'si5p5QoINvA', 'Si6yUaMM2c8', 'sIYzY8jnifU', 'SjrIit0fYgo', 'SlqZsorw7rI',
                 'sn1pZ7H66Do', 'sO6Ahl1FCy4', 'SOeFRkaRccg', 'SPxisxSv-dM', 'SQ0d25LZnH8', 'SQm4M4GCtOk', 'SQ_h3EVhqfw', 'sr9KfphbgQE',
                 'SSFkoA3qt68', 'SsLsuDtaDmE', 'sTfoh0vRA08', 'Sti-LQuAG1k', 'StTuvR_l-OY', 'SUB0hybpY-Y', 'sueclA2NVao', 'SuxxtZjVLCk',
                 'svW_04e1Oi8', 'SWHSKLlVDys', 'swIVXa6k-AE', 'swzxvMXz93I', 'sXOQ9VaYEv0', 'SxpnXcfInUE', 'SX_bbPvbKMM', 'SyafDOQNGl8',
                 'sYjHK5b7Jzs', 'Syp8hZuLLb4', 'szVxktVaiYk', 's_20-g15v54', 't0c8Yp_anAE', 'T0xtOAmKhdA', 't26NpV2d98s', 'T3COi_qVfMU',
                 't3lXPKgBm8k', 'T4NWm7mqbHI', 'T6ZDBpVSg3U', 'T7OVrWn1mp4', 'T8gxRDL7ig4', 'T8MNDHUhK_Y', 'tbdGw97gVMA', 'tbheA9rm-vY',
                 'tbW8djVi83o', 'tC21KpcPe2U', 'Tcqb74Vz7B8', 'tDETBkJIUJ8', 'tdfOnsNkWE4', 'te0qNl30VdM', 'TEkATzoxLYA', 'TH1IVwZmAEE',
                 'thb7LGhu-uk', 'TjMAUIAk_-s', 'tLi1PZSyk3o', 'tlQAHvtYZb0', 'tngxTE8Oayg', 'TNKRk0WRJqc', 'TNr-P1292F8', 'TnX6dlE09bM',
                 'To-KPRqE0_w', 'tP8SXuK2veI', 'TPEWDNC5tLw', 'TPXi_WEWM_U', 'TS_AG7lHr3E', 'TUwd4ZHgd2w', 'TVXRY2FVOEM', 'TwtcKKt4i94',
                 'Tx17kzQGqlg', 'TXDXwlptGXs', 'ty0unGK71Hw', 'TZ6xeS_GjSk', 'TZKn9CcJ-Y4', 'U0EgpdFjQCI', 'U52oraqTGWU', 'u59Zly1rr1Y',
                 'u6CV5SADa34', 'u6dT3LVfZl4', 'u7us_YSKRDA', 'U8kUTZXyDfU', 'u8ZL0XLXA54', 'UajIZXrSUq8', 'uAk9ppD-KZk', 'uAMJi-RMimI',
                 'UcHqSfrekBs', 'UcNH7ub6iOQ', 'ucpj5J7H9jA', 'uCUwB1t2sLA', 'udqv-3og9_k', 'udxHIUUzrRk', 'ue96cuS-lNs', 'UEVVUpz30RQ',
                 'uEYMYd8xA8Q', 'uFyuiJEd60w', 'UgQHjFZvR0M', 'UH1yTqt1sK8', 'uIvdELL9its', 'UjPldsSfiQU', 'uK9oG68ajq8', 'ukuK87Tfgx0',
                 'ukYrii2Ap6k', 'uLabZemWGMk', 'ULXVP5b22yw', 'UM1wMCspFRI', 'umcmHk789Ag', 'UNEv7OurotE', 'uOGLQsEWeIY', 'uP0G9G8Wfp0',
                 'UpY_lyC2DKg', 'Uqa30vUUw0g', 'uRlAUI2l3dA', 'uRmLT6KXMas', 'USK-41GxCRc', 'uSZwWPCuh0M', 'uT9vOC6lm_w', 'UTAyLrpNkaE',
                 'utV0ejirsTI', 'UU2Zy6Q6eDg', 'uuuXnAr_7iY', 'UvdoHPneyRE', 'UwgAmmI6rQw', 'UWSPIHGiuFs', 'uxghTmNb0pU', 'UxJEYN7MB2M',
                 'uY3DU3N15kc', 'UY8CCr_Ec6w', 'v-u3UcnxLJY', 'v00xAgLkB-k', 'V2N6MXL3RrE', 'V2NApvhoWh4', 'V2p6Kr-ru1M', 'V44OI-FjBCk',
                 'v6-3Fw1t4H8', 'v6zAy9krPjM', 'V8pJulMlBmk', 'va6R3N2fRE8', 'vAhCS89Wznc', 'VaUTYwC5how', 'VbdI4kIAEVU', 'vBQaeq2vLsw',
                 'Vbz3eG9WmEE', 'vdbghI49kzk', 'VFSHUlQEE80', 'Vg7Mwy5RK-g', 'VHjUH7yXiJU', 'vhVQk4GeMrI', 'vIAgrwEm2Lk', 'Vij41V3rMEc',
                 'VikRTpwgyeo', 'VILzeB68orc', 'vKmGbEkDcfg', 'VmWZSryeMjs', 'vnmL_X6csSA', 'VPGLhcM7r94', 'VpsDihMedU8', 'vQ5UuZsZ70w',
                 'vR0_BaXYcE4', 'vRZF5P_0lqk', 'vTOUir5_V_0', 'vvD-fKq8IyM', 'VVkhY8mUPaY', 'Vvr2T-wSIdk', 'Vww-G6oObTA', 'vX3CJKueq18',
                 'vxnveaa9GYI', 'VZeZREFZVXU', 'v_4amQy8u5c', 'w0m4jqyWTN8', 'W0vr0rQ7r7Y', 'w1A20nBbG3s', 'w1cUrdYOdRg', 'w1XCWyF6m48',
                 'W63vrbX-mLg', 'w6UsbBX2goQ', 'w8QIDk8KQ4I', 'W96Y1crspIw', 'WbUFFhsEhZM', 'wCxr-cL03ys', 'WDsbUWJkjWI', 'wDuyrjczdbg',
                 'weW6D4jz0Zg', 'WgdSkUtD_fs', 'winSCwuAu0c', 'WISzaCdJSQg', 'wji8Y3zdbU8', 'wKCPiSnYqwA', 'WKIHPbVVmuo', 'wlssXdkjCLs',
                 'wMbegc0txx4', 'WMMv2nR5Qeg', 'wN3Bmhhohjk', 'WneRaj75II4', 'WO8qxFxtB1U', 'wohEnR5zve0', 'WoJ8EGzwj_g', 'wOzCkcGbcAw',
                 'wP1_CqcEV5Y', 'wpG4la-iUJ8', 'WPgcEBhbtsg', 'WpZqLbWL0c0', 'wsBy4sG2TQY', 'WSjN5gPJ-UU', 'wsxhWqjGfns', 'WtboYBheeco',
                 'wuc_OBcehjo', 'WXapdvfTgas', 'wXjQHAxopzk', 'wXJRBD_7Xvo', 'WxOAbjhYZck', 'wygzSdI0L1Q', 'wyWf2uYOKYU', 'wZeXFV4V318',
                 'WZgh0hgEJxE', 'WZvIw0SnYrE', 'x41zyB73ZHI', 'x4vRQ_jSJJ0', 'x65KrFFQPpw', 'x9Nd6OZV-Yk', 'X9Qfzn5vgHs', 'xAfKZrAYORg',
                 'XaLHd7nx330', 'XcU6g_ppWRI', 'xdi9mCRZnY4', 'xEEw2wR-Mck', 'xEfAF4M8sis', 'XeMwoMk8wSw', 'xfPdbz3qPT0', 'xFXDhDkBDbw',
                 'xG_BYaIugPg', 'XhgN5clDnXw', 'xhOLC-JvJ68', 'xjqXZhbaWIs', 'XjXm-ELojYI', 'Xkix8uweNsc', 'xKQgB6ODAeY', 'xLIFT9xoWSQ',
                 'Xmmw9g4eNqs', 'xnb7MbXEcDM', 'XnGIUJWMCno', 'xofnnPS2KyY', 'XoGpnJ2_t2A', 'xOhTNHHWcMc', 'xQaO94_p6pc', 'XRSI-Yu4NEM',
                 'xs-ndwYLFRw', 'XsoVSDpD_7o', 'xsqaL7c22q8', 'XTCtlupUbCA', 'xtPonlDtQlk', 'XUuTSVgAAFc', 'xvo_4RpdNJU', 'xwJOXomT1jk',
                 'XztBUNsMQ2c', 'Y-r9hjRY1DM', 'Y3qj40IrPvo', 'y4_y-QqnV14', 'Y5HOvK_4pGk', 'y63nHZQZucA', 'Y64hvw0kZig', 'Y85VZlSCJCo',
                 'y8zFfIZcaWs', 'y9JAopB6OqQ', 'yA3AD9jU7QU', 'YAeQAF-WzZc', 'YAr31WmHbVU', 'yAyOVxAwm78', 'ycQs27YVE60', 'YdiF7c9a19o',
                 'yDUoc9gHb9c', 'YeXollGBQ8Y', 'yfazGm58-MI', 'yg9uopmNeUU', 'yhmWLvrz61k', 'YIo0ULHsvYY', 'yKu33AsV4z0', 'Yl7vFm9sZYA',
                 'YLMPAtkg-Kk', 'yltZSEcAylA', 'ym3gp7IwmUo', 'ymIyKGqwwpA', 'YmOrsKpn3FM', 'yNAPdZ-SiOU', 'YNfawBvbtcE', 'ynYZyE9GFfs',
                 'YO3r9NRdEkY', 'YPFpKPqMhS8', 'Yq-FTeXZkvM', 'YqewLkWns_o', 'yQfNBx-NP9o', 'YQIK9BRt6HI', 'yqxRWefytyY', 'YRrJqyh7OfQ',
                 'ysGgGuL7B8s', 'YTEniEh6uS0', 'yTexe1HgJtU', 'YTv0BlQp36A', 'YU832gzgifo', 'yUul5smwack', 'yuvRc1aBc_w', 'yWg58bqVvms',
                 'YWN1PpNUIfM', 'YwOQinOq9pg', 'yYgIkj2ebP8', 'YywoU3jetMU', 'YZNM6cMMY1E', 'yzSB1yKD6JM', 'YZyCgRF6JrE', 'y_qoXSYt11I',
                 'z1SJTeRYKUg', 'Z3y2cZVJJus', 'Z5Lx--xlj28', 'z5PZXA1zqA4', 'Z6Sr3Rk1k-8', 'z84NmFZYbpU', 'Z8rkp1cEyTE', 'ZabDAaRV0Y8',
                 'zAV6Nl2sKws', 'ZBsKr3PMp4E', 'Zc8Ulx0n7XQ', 'zE3TnNspVWg', 'zevN6AlhH_s', 'ZeWGuUbdnTU', 'ZFDQ2VMMXZY', 'Zfl741QO3Ag',
                 'zFUtNpxVwH4', 'zJi8m4buMrw', 'zJjbOZUIIPQ', 'zKSxuFD9Jpc', 'zKV5zMRHOig', 'ZL46IjBH7L0', 'zlmHuO5TBDY', 'zls5pP7OgOM',
                 'zLY1WkaXzP0', 'ZL_HGe8TsBY', 'zmao_p5nPMs', 'ZmxXsM_Gz3w', 'zNCR5WPhxOA', 'ZNji1mnSB8g', 'znJWfiogjtQ', 'zNQqchIJe0o',
                 'ZONwGb7YGrk', 'zp4adGsyopE', 'zqDAotkTwrs', 'zQVt-1gUALU', 'zqZ1n_xSJfE', 'zR2yqPfw7UM', 'zR6hzzDAflI', 'zRucPU7bGsA',
                 'zSU8dvbdKnU', 'ZtmLdYTVszA', 'Zu81phMB9rk', 'ZVRp-8w3qhI', 'Zw0jo3SePtA', 'zWyQW8YIIf8', 'zXmO5_tiuM0', 'Zxn9X6XXOnU',
                 'ZxRlWfvn6Dk', 'zyr1F12AuAY', 'zz7x23rrwl8', '_0z11rWXLrg', '_1507-Lo6Eg', '_6DU0pPzzoY', '_7MBer1SeCM', '_AL1EoJWM5s',
                 '_Bj0FbjFFJY', '_bu8Bb7XV5U', '_bXiwiVKfGs', '_c4dKyR3enc', '_dwL-FO2NLk', '_EctlaeJjuo', '_f46uY1hvC0', '_HbecwTgugc',
                 '_htrPTOvX-s', '_K4phsNsy5U', '_KzjEAGue1U', '_nD1eYhp9NQ', '_rTq99Y8T_w', '_S8JfTbZbdk', '_yxBZ4qJNe8', '_Zj47bS5auo',
                 '_Zocs3SxShk', '__Oe9dJ3ZZ0']

    failed_videos = download_videos(video_ids, output_path)

    if failed_videos:
        print('Video IDs unable to download:')
        for video_id in failed_videos:
            print(video_id)
    else:
        print('All videos downloaded successfully!')
