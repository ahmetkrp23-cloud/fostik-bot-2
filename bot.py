import discord
from discord.ext import commands
import random


# -----------------------------
# AYARLAR
# -----------------------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="$",
    intents=intents,
    help_command=None
)


# -----------------------------
# BOT HAZIR
# -----------------------------

@bot.event
async def on_ready():
    print("Fostik Bot olarak giriş yaptık.")
    print("Bot aktif.")


# -----------------------------
# NORMAL MESAJLAR
# -----------------------------

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    mesaj = message.content.lower()

    if mesaj.startswith("merhaba"):
        await message.channel.send("Selam kral! 😎")

    elif mesaj.startswith("selam"):
        await message.channel.send("Aleyküm selam! 👋")

    elif mesaj.startswith("$bye"):
        await message.channel.send("Görüşürüz kral! 👋")

    elif mesaj.startswith("$şifre ne?"):
        await message.channel.send("fostikoo8")

    elif not message.content.startswith("$"):
        await message.channel.send(message.content)

    await bot.process_commands(message)


# -----------------------------
# SELAM
# -----------------------------

@bot.command()
async def selam(ctx):
    await ctx.send("Selam kral! 😎")


# -----------------------------
# HEH
# -----------------------------

@bot.command()
async def heh(ctx, sayi: int = 5):

    if sayi < 1:
        await ctx.send("En az 1 yazmalısın.")
        return

    if sayi > 50:
        await ctx.send("En fazla 50 tane yapabilirsin.")
        return

    await ctx.send("he" * sayi)


# -----------------------------
# MEME
# -----------------------------

@bot.command()
async def mem(ctx):

    with open("images/mem1.webp", "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def mem2(ctx):

    with open("images/mem2.webp", "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def mem3(ctx):

    with open("images/mem3.webp", "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


# -----------------------------
# NADİR MEME SİSTEMİ
# ÖDEV
# -----------------------------

@bot.command()
async def rastgelemem(ctx):

    memler = [
        "images/mem1.webp",
        "images/mem2.webp",
        "images/mem3.webp"
    ]

    nadirlikler = [
        60,
        30,
        10
    ]

    secilen_mem = random.choices(
        memler,
        weights=nadirlikler,
        k=1
    )[0]

    with open(secilen_mem, "rb") as f:
        picture = discord.File(f)

    await ctx.send(
        "🎲 Rastgele bir meme seçtim!\n"
        "🍀 Nadirlik sistemi kullanıldı.",
        file=picture
    )


# -----------------------------
# YARDIM
# -----------------------------

@bot.command(name="yardım")
async def yardim(ctx):

    embed = discord.Embed(
        title="🤖 FOSTİK BOT",
        description="Kullanabileceğin komutlar aşağıda!",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="💬 Eğlence",
        value=(
            "`$selam` → Bot selam verir\n"
            "`$heh 10` → 10 kere he yazar\n"
            "`$zar` → Zar atar\n"
            "`$yazitura` → Yazı veya tura atar\n"
            "`$8ball soru` → Soruna cevap verir\n"
            "`$kura @kişi @kişi` → Kura çeker\n"
            "`$mem` → Meme 1\n"
            "`$mem2` → Meme 2\n"
            "`$mem3` → Meme 3\n"
            "`$rastgelemem` → Nadirlik sistemli rastgele meme"
        ),
        inline=False
    )

    embed.add_field(
        name="👤 Bilgi",
        value=(
            "`$oyuncu` → Kendi bilgilerini gösterir\n"
            "`$sunucu` → Sunucu bilgilerini gösterir\n"
            "`$avatar` → Profil fotoğrafını gösterir\n"
            "`$ping` → Botun pingini gösterir"
        ),
        inline=False
    )

    embed.add_field(
        name="🛠️ Moderasyon",
        value=(
            "`$sil 5` → 5 mesaj siler\n"
            "`$at @kişi` → Üyeyi sunucudan atar\n"
            "`$yasakla @kişi` → Üyeyi yasaklar"
        ),
        inline=False
    )

    embed.add_field(
        name="🤖 Diğer",
        value=(
            "`merhaba` → Bot cevap verir\n"
            "`selam` → Bot cevap verir\n"
            "`$bye` → Bot veda eder"
        ),
        inline=False
    )

    embed.set_footer(
        text="Fostik Bot • Kodland Projesi"
    )

    await ctx.send(embed=embed)


# -----------------------------
# ZAR
# -----------------------------

@bot.command()
async def zar(ctx):

    sayi = random.randint(1, 6)

    await ctx.send(
        "🎲 {} zar attı!\n"
        "Sonuç: **{}**".format(
            ctx.author.name,
            sayi
        )
    )


# -----------------------------
# YAZI TURA
# -----------------------------

@bot.command()
async def yazitura(ctx):

    sonuc = random.choice([
        "YAZI 🪙",
        "TURA 🪙"
    ])

    await ctx.send(
        "🪙 {} attı!\n"
        "Sonuç: **{}**".format(
            ctx.author.name,
            sonuc
        )
    )


# -----------------------------
# 8BALL
# -----------------------------

@bot.command(name="8ball")
async def eightball(ctx, *, soru=None):

    if soru is None:
        await ctx.send(
            "🎱 Bir soru sormalısın!\n"
            "Örnek: `$8ball bugün şanslı mıyım?`"
        )
        return

    cevaplar = [
        "Kesinlikle! 😎",
        "Bence evet! ✅",
        "Büyük ihtimalle. 🤔",
        "Olabilir. 👀",
        "Emin değilim. 🤷",
        "Pek sanmıyorum. 😅",
        "Hayır. ❌",
        "Kesinlikle hayır! 😂",
        "Tekrar sor. 🎱"
    ]

    cevap = random.choice(cevaplar)

    embed = discord.Embed(
        title="🎱 Fostik 8Ball",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="❓ Soru",
        value=soru,
        inline=False
    )

    embed.add_field(
        name="🔮 Cevap",
        value=cevap,
        inline=False
    )

    await ctx.send(embed=embed)


# -----------------------------
# KURA
# -----------------------------

@bot.command()
async def kura(ctx, uyeler: commands.Greedy[discord.Member]):

    if len(uyeler) < 2:
        await ctx.send(
            "🎯 En az 2 kişi etiketlemelisin!\n"
            "Örnek: `$kura @Ahmet @Mehmet`"
        )
        return

    kazanan = random.choice(uyeler)

    isimler = []

    for uye in uyeler:
        isimler.append(uye.mention)

    embed = discord.Embed(
        title="🎯 KURA SONUCU",
        color=discord.Color.gold()
    )

    embed.add_field(
        name="👥 Katılanlar",
        value=", ".join(isimler),
        inline=False
    )

    embed.add_field(
        name="🏆 Kazanan",
        value=kazanan.mention,
        inline=False
    )

    await ctx.send(embed=embed)


# -----------------------------
# OYUNCU BİLGİLERİ
# -----------------------------

@bot.command()
async def oyuncu(ctx):

    uye = ctx.author

    embed = discord.Embed(
        title="👤 Oyuncu Bilgileri",
        color=discord.Color.green()
    )

    embed.add_field(
        name="👤 Kullanıcı",
        value=uye.name,
        inline=False
    )

    embed.add_field(
        name="🆔 ID",
        value=str(uye.id),
        inline=False
    )

    embed.add_field(
        name="📅 Hesap oluşturulma",
        value=uye.created_at.strftime("%d.%m.%Y"),
        inline=False
    )

    embed.set_thumbnail(
        url=uye.display_avatar.url
    )

    await ctx.send(embed=embed)


# -----------------------------
# SUNUCU BİLGİLERİ
# -----------------------------

@bot.command()
async def sunucu(ctx):

    if ctx.guild is None:
        await ctx.send(
            "Bu komut sadece bir Discord sunucusunda kullanılabilir."
        )
        return

    sunucu = ctx.guild

    embed = discord.Embed(
        title="🏠 Sunucu Bilgileri",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="🏠 Sunucu",
        value=sunucu.name,
        inline=False
    )

    embed.add_field(
        name="👥 Üye sayısı",
        value=str(sunucu.member_count),
        inline=False
    )

    embed.add_field(
        name="💬 Kanal sayısı",
        value=str(len(sunucu.channels)),
        inline=False
    )

    embed.add_field(
        name="👑 Sunucu sahibi",
        value=str(sunucu.owner),
        inline=False
    )

    await ctx.send(embed=embed)


# -----------------------------
# AVATAR
# -----------------------------

@bot.command()
async def avatar(ctx):

    uye = ctx.author

    embed = discord.Embed(
        title="🖼️ Avatar",
        description="{} kullanıcısının profil fotoğrafı".format(
            uye.name
        ),
        color=discord.Color.blue()
    )

    embed.set_image(
        url=uye.display_avatar.url
    )

    await ctx.send(embed=embed)


# -----------------------------
# PING
# -----------------------------

@bot.command()
async def ping(ctx):

    ping = round(bot.latency * 1000)

    if ping < 100:
        durum = "🟢 Çok iyi!"
    elif ping < 200:
        durum = "🟡 İyi."
    else:
        durum = "🔴 Yüksek."

    await ctx.send(
        "🏓 Pong!\n"
        "📡 Ping: **{} ms**\n"
        "{}".format(
            ping,
            durum
        )
    )


# -----------------------------
# MESAJ SİL
# SADECE YETKİLİ
# -----------------------------

@bot.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx, miktar: int = 1):

    if miktar < 1:
        await ctx.send("En az 1 mesaj silebilirsin.")
        return

    if miktar > 100:
        await ctx.send("Tek seferde en fazla 100 mesaj silebilirsin.")
        return

    await ctx.channel.purge(
        limit=miktar + 1
    )

    mesaj = await ctx.send(
        "🗑️ {} mesaj silindi.".format(miktar)
    )

    await mesaj.delete(delay=3)


# -----------------------------
# ÜYE AT
# SADECE YETKİLİ
# -----------------------------

@bot.command()
@commands.has_permissions(kick_members=True)
async def at(ctx, member: discord.Member):

    if member == ctx.author:
        await ctx.send(
            "😂 Kendini sunucudan atamazsın."
        )
        return

    if member == ctx.guild.owner:
        await ctx.send(
            "👑 Sunucu sahibini atamazsın."
        )
        return

    try:
        await member.kick()

        await ctx.send(
            "👢 {} sunucudan atıldı.".format(
                member
            )
        )

    except discord.Forbidden:
        await ctx.send(
            "⛔ Bu üyeyi atamıyorum. Botun yetkisini veya rol sırasını kontrol et."
        )


# -----------------------------
# ÜYE YASAKLA
# SADECE YETKİLİ
# -----------------------------

@bot.command()
@commands.has_permissions(ban_members=True)
async def yasakla(ctx, member: discord.Member):

    if member == ctx.author:
        await ctx.send(
            "😂 Kendini yasaklayamazsın."
        )
        return

    if member == ctx.guild.owner:
        await ctx.send(
            "👑 Sunucu sahibini yasaklayamazsın."
        )
        return

    try:
        await member.ban()

        await ctx.send(
            "🔨 {} sunucudan yasaklandı.".format(
                member
            )
        )

    except discord.Forbidden:
        await ctx.send(
            "⛔ Bu üyeyi yasaklayamıyorum. Botun yetkisini veya rol sırasını kontrol et."
        )


# -----------------------------
# KOMUT HATALARI
# -----------------------------

@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.MissingPermissions):

        await ctx.send(
            "⛔ Bu komutu kullanmak için gerekli yetkin yok."
        )

    elif isinstance(error, commands.MissingRequiredArgument):

        await ctx.send(
            "❌ Gerekli bir bilgi eksik."
        )

    elif isinstance(error, commands.BadArgument):

        await ctx.send(
            "❌ Girdiğin kişi veya bilgi hatalı."
        )

    elif isinstance(error, commands.CommandNotFound):

        pass

    else:
        print(
            "Hata:",
            error
        )


# -----------------------------
# BOTU ÇALIŞTIR
# -----------------------------

bot.run("token(:")