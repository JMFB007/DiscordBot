from discord.ext import commands
import random

import time
from datetime import datetime

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="Roll", aliases=["roll","rolls"], brief="Rolls a dice")
  async def roll(self, ctx, *, args=None):
    try:
      times,die = args.split("d",1)
      plus = "0"
      if times == "":
        times = "1"
      if "+" in die:
        die,plus = die.split("+")
      print(times +" "+ die +" "+ plus)
      rolls = []
      for n in range(int(times)):
        rolls.append(str(random.randint(1,int(die))+plus))
      s = "`, `".join(rolls)
      if len(s)>(4000-9):
        await ctx.send("Too many rolls to send")
      else:
        await ctx.send(f"Rolls: `{s}`")
    except:
      await ctx.send("Message sent in an invalid way, please do `-roll d<dice>` or `<times>d<dice>` or `<times>d<dice>+<bonus>`")

  @commands.command(name="Random", aliases=["random"], brief="Shows a random number between 2 values")
  async def random(self, ctx, argi=None, argf=None):
    if (argi and argf) != None and argi.isdigit() and argf.isdigit():
      if argi>argf:
        x = 0
        x = argi
        argi = argf
        argf = x
      await ctx.send(f"Random number: `{random.randint(int(argi),int(argf))}`")
    else:
      await ctx.send("Please insert 2 numbers `-random # #`")
      
  @commands.command(name="Insult", aliases=["insult", "insulto","Insulto"], brief="Sends an insult in spanish")
  async def insult(self, ctx, arg1 = None, arg2 = None):
    insults =["Aberracion" ,"Aberración" ,"Aberrante" ,"Ablanda brevas" ,"Abollao" ,"Aborto" ,"Abrillantaglandes" ,"Abulto","Afilasables" ,"Aguafiestas" ,"Alcachofo" ,"Alcornoke" ,"Alcornoque" ,"Alimaña" ,"Amorfo" ,"Analfabestia" ,"Animal de acequia" ,"Anormal" ,"Aragán" ,"Arrastramantas" ,"Arrastrazapatillas" ,"Arrollapasto" ,"Artosopas" ,"Asalta asilos" ,"Asaltacunas" ,"Asaltapozos" ,"Aspamao" ,"Asustatrenes" ,"Atonta","Atontada" ,"Atontado" ,"Atontao","Atroplella platos" ,"Baboso" ,"Bacterio" ,"Bailabainas" ,"Bailaferias" ,"Bandarra" ,"Barjaula" ,"Barriobajero" ,"Bastarda" ,"Bastardo" ,"Bebecharcos" ,"Bebesinsed" ,"Bellaco" ,"Bergante" ,"Berzotas" ,"Besugo" ,"Bigardo" ,"Bigotezorra","Biruta" ,"Bleda" ,"Boba" ,"Bobo" ,"Bobolaverga" ,"Bobomierda" ,"Boborremoto" ,"Bocabuzón" ,"Bocachancla" ,"Bocachocho" ,"Bolascombro" ,"Boludo" ,"Borracha" ,"Borracho" ,"Borrico" ,"Bosses tristes" ,"Boñiga" ,"Brasas" ,"Brincacepas" ,"Burreras" ,"Burro de set soles" ,"Buscabregues" ,"Cabeza alberca" ,"Cabeza de chorlito" ,"Cabezabuque" ,"Cabezakiko" ,"Cabezalpaca" ,"Cabezantorcha" ,"Cabezarrucho" ,"Cabezon" ,"Cabezón" ,"Cabron" ,"Cabrona" ,"Cabronazo" ,"Cabrón" ,"Cacho mierda" ,"Cachomierda" ,"Caga bandurrias" ,"Cagablando" ,"Cagadubtes" ,"Cagaestacas" ,"Cagaportales" ,"Cagarro" ,"Caharrán" ,"Calamidad" ,"Calenturas" ,"Calvo" ,"Calzonazos" ,"Canalla" ,"Cansa almas" ,"Cansaliebres" ,"Capulla" ,"Capullo" ,"Capuyo" ,"Cara de cona" ,"Caracabello" ,"Caracandao" ,"Caracartón" ,"Carachancla" ,"Caracoño" ,"Caracul" ,"Caraculo" ,"Caraespatula" ,"Caraestaca" ,"Caraestufa" ,"Caraflema" ,"Carajaula" ,"Carajote" ,"Caramierda" ,"Caranabo" ,"Carantigua" ,"Carapan" ,"Carapapa" ,"Carapena" ,"Caraperro" ,"Carapolla" ,"Caraputa" ,"Carasapo" ,"Carasuela" ,"Cascavalero" ,"Cateto" ,"Cebollino" ,"Cenizo" ,"Cenutrio" ,"Cerillita" ,"Cero a la izquierda" ,"Chafacharcos" ,"Chafalotodo" ,"Chalada" ,"Chalado" ,"Chalao" ,"Chavacana" ,"Chavacano" ,"Chavea" ,"Cheo de moscas" ,"Chichon" ,"Chimpa" ,"Chingada" ,"Chorlito" ,"Chosco" ,"Chupacables" ,"Chupacharcos" ,"Chupaescrotos" ,"Chupamela" ,"Chupamingas" ,"Chupasangre" ,"Chupatintas" ,"Cierrabares" ,"Ciervo" ,"Cobarde" ,"Comebolsas" ,"Comechapas" ,"Comemierda" ,"Comemierdas" ,"Comemocos" ,"Comepollas" ,"Comeprepucios" ,"Cornudo" ,"Cretina" ,"Cretino" ,"Crollo" ,"Cuerpoescombro" ,"Culo panadera" ,"Culoalberca" ,"Culotrapo" ,"Desaborio" ,"Descalzaputas" ,"Descerebrado" ,"Desgracia" ,"Desgraciada" ,"Desgraciado" ,"Desgraciao" ,"Despreciable" ,"Destiñe rubias" ,"Desvarata bailes" ,"Desvirgagallines" ,"Don nadie" ,"Donnadie" ,"Down" ,"Durdo" ,"Empaellao" ,"Empana" ,"Empanao" ,"Empujamierda" ,"Enderezaplátanos" ,"Engendro" ,"Enrreda bailes" ,"Escoria" ,"Escuerzo" ,"Escuincle" ,"Espantacriatures" ,"Espantajo" ,"Esperpento" ,"Estas como un manojo de vergas" ,"Estorbo" ,"Estupida" ,"Estupido" ,"Estòtil" ,"Estúpida" ,"Estúpido" ,"Eunuco" ,"Facha" ,"Fanicerós" ,"Fantoche" ,"Fariseo" ,"Farsante" ,"Fea" ,"Feminazi" ,"Feo" ,"Feodoble" ,"Feto" ,"Follacabras" ,"Follagatos" ,"Follácaros" ,"Fune" ,"Funesto" ,"Ganapán" ,"Gansa" ,"Ganso" ,"Gilipollas" ,"Gonorrea" ,"Gordinflón" ,"Gordo" ,"Granuja" ,"Grosera" ,"Grosero" ,"Gusano" ,"Hdp" ,"Hijo de puta" ,"Hijo de chacal" ,"Hijo de cura" ,"Hijo de hiena" ,"Hijo de obispo" ,"Hijueputa" ,"Horripilante" ,"Huelebragas" ,"Huevon" ,"Huevón" ,"Idiota" ,"Ignorante" ,"Imbecil" ,"Imbécil" ,"Impertinente" ,"Inculto" ,"Inelegante" ,"Infraser" ,"Inoperante" ,"Inutil" ,"Inútil" ,"Jartible" ,"Jodido" ,"Lameculos" ,"Lamehuevos" ,"Lameplatos" ,"Lamerajas" ,"Lameñordos" ,"Lechuguino" ,"Lela" ,"Lelo" ,"Lento" ,"Ligera de cascos" ,"Ligero de cascos" ,"Llimpiatubos" ,"Machirulo" ,"Machorra" ,"Machote" ,"Mal pelat" ,"Malafoyao" ,"Malandra" ,"Malandrin" ,"Malasangre" ,"Maleducao" ,"Maleducada" ,"Maleducado" ,"Maleducao" ,"Malfollada" ,"Malnacida" ,"Malnacido" ,"Malparida" ,"Malparido" ,"Mamacallos" ,"Mamahostias" ,"Mamon" ,"Mamona" ,"Mamón" ,"Manos Gachas" ,"Maricón" ,"Marimacho" ,"Masturbamulos" ,"Masturbaperros" ,"Masturbavacas" ,"Matao" ,"Mataperros" ,"Me cago en tu madre" ,"Me cago en tu padre" ,"Me cago en tu puta madre" ,"Me cago en tu puto padre" ,"Me cago en tus muertos" ,"Media mierda" ,"Meketrefe" ,"Mema" ,"Memo" ,"Mequetrefe" ,"Merda" ,"Merda seca" ,"Merdaseca" ,"Microbio" ,"Mierda" ,"Mierdaseca" ,"Mofeta" ,"Mojigato" ,"Monchi" ,"Mondongo" ,"Monte de estercol" ,"Muerdealmohadas" ,"Muggle" ,"Mugrosa" ,"Mugroso" ,"Necia" ,"Necio" ,"Niñato" ,"Osobuco" ,"Otaco" ,"Otako" ,"Otaku" ,"Otakus" ,"Pajera" ,"Pajero" ,"Palotrasto" ,"Pambisita" ,"Pambisito" ,"Pamplinas" ,"Panojas" ,"Papagayo" ,"Papanatas" ,"Paquete" ,"Pardal" ,"Pataliebre" ,"Patan" ,"Patasdealambre" ,"Patetica" ,"Patetico" ,"Patán" ,"Patética" ,"Patético" ,"Payasa" ,"Payaso" ,"Pecholata" ,"Pechopertiga" ,"Pechugona" ,"Peinaburras" ,"Peinaobejas" ,"Peinaovejas" ,"Pelacañas" ,"Pelagatos" ,"Pelalimones" ,"Pelamangos" ,"Pelarrabos" ,"Pelele" ,"Pelo estropajo" ,"Pelotudo" ,"Pendejo" ,"Percebe","Picapleitos" ,"Pichabrava" ,"Pichacorta" ,"Pimpoyo" ,"Pinchacolillas" ,"Pinche" ,"Pintamonas" ,"Piojoso" ,"Pipa" ,"Pipilla" ,"Pipiolo" ,"Pitufo" ,"Plasta" ,"Plumifero" ,"Pocasluces" ,"Pocasolta" ,"Pregonao" ,"Pringazorras" ,"Pudrecolchones" ,"Puta" ,"Putos" ,"Puto" ,"Rabo" ,"Rata" ,"Repelente" ,"Retardado" ,"Retrasado" ,"Retrasubnormal" ,"Retropetuda" ,"Robaperas" ,"Ruda" ,"Rudo" ,"Rufían" ,"Ruina" ,"Sabandija" ,"Sangre sucia" ,"Sanguijuela" ,"Santurron" ,"Santurrona" ,"Santurrón" ,"Sarnoso" ,"Seboso" ,"Sinsorgo" ,"Sinsustancia" ,"Soplagaitas" ,"Soplanucas" ,"Soplasartenes" ,"Subnormal" ,"Subnormala" ,"Subnormalo" ,"Subnorpollas" ,"Sunormal" ,"Tacaño" ,"Tarado" ,"Tastaolletes" ,"Te huele la espalda a baron dandi" ,"Tocapelotas" ,"Tonta" ,"Tontaco" ,"Tonto" ,"Tonto dels collons" ,"Tontoculo" ,"Tontoelculo" ,"Tontolculo" ,"Tontoloscojones" ,"Tontopolla" ,"Tontoprofundo" ,"Tontucio" ,"Tragalefas" ,"Tragalpacas" ,"Trasto" ,"Troglodita" ,"Tuercebotas" ,"Vandalo" ,"Vendehumos" ,"Verga" ,"Votante del PP" ,"Vándalo" ,"Zanahorio" ,"Zangano" ,"Zangüángano" ,"Zarandajo" ,"Zarrapastrosa" ,"Zarrapastroso" ,"Zopenco" ,"Zoquete" ,"Zorra" ,"Zumbado" ,"Zumbao" ,"Zángano"]
    try:
      if arg1 == None:
        await ctx.send(insults[random.randint(0,len(insults)-1)])
      else:
        if arg2 == None:
          await ctx.channel.purge(limit = 1)
          await ctx.send(insults[random.randint(0,len(insults)-1)] 
   + f" {arg1}")
        elif isinstance(arg2,int):
          ins = []
          for i in range(int(arg2)):
            ins.append(insults[random.randint(0,len(insults)-1)])
          s = ", ".join(ins)
          await ctx.channel.purge(limit = 1)
          await ctx.send(s + f" {arg1}")
        else:
          await ctx.send("Please format like this: `-insult @<Person> <number>`")
    except:
      await ctx.send("Please format like this: `-insult @<Person> <number>`")

  @commands.command(name="Test", aliases=["test"], brief="Test for times stuff")
  async def test(self, ctx, hora=None, minuto=None):
    if hora != None and hora.isdigit() and minuto != None and minuto.isdigit():
      hora = int(hora)
      minuto = int(minuto)
      if hora>24 or hora<0:
        await ctx.send("La hora tiene que ser entre 00 y 24")
        return#verificar
      if minuto>59 or minuto<0:
        await ctx.send("Los minutos tienen que estar entre 00 y 59")
        return
      #tiempo = datetime.replace(hour=hora, minute=minuto)
      #while True:
      await ctx.send(f"tiempo:")
      time.sleep(60)
      await ctx.send(f"tiempo:")
    else:
      await ctx.send("Hacer `-test <hora> <minuto>`")
    
def setup(bot):
  bot.add_cog(Fun(bot))